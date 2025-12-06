import sys
import os
import io
import time
import threading
import webbrowser
import gc  # Garbage Collector interface
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from typing import Optional, Callable

# Third-party imports
from PIL import Image, ImageTk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# --- BACKEND ENGINE WITH RESOURCE WATCHDOG ---
class ScreenshotEngine:
    def __init__(self):
        self.driver = None
        self.lock = threading.Lock() # Thread safety mechanism
        self.last_used_time = time.time()
        self.cleanup_timeout = 120  # 2 Minutes limit
        
        # Start the Watchdog
        self.running = True
        self.watchdog_thread = threading.Thread(target=self._resource_watchdog, daemon=True)
        self.watchdog_thread.start()

    def _resource_watchdog(self):
        """
        Runs in background. Checks every 10s if the driver has been idle 
        for more than 2 minutes. If so, kills it to free RAM.
        """
        while self.running:
            time.sleep(10)
            with self.lock:
                # If driver exists AND time since last use > 120s
                if self.driver and (time.time() - self.last_used_time > self.cleanup_timeout):
                    print("[Watchdog] Inactivity detected (2min). releasing resources...")
                    try:
                        self.driver.quit()
                    except:
                        pass
                    self.driver = None
                    # Force Python to clean up memory immediately
                    gc.collect()
                    print("[Watchdog] Memory cleaned.")

    def init_driver(self):
        """Initializes Chrome. Thread-safe."""
        with self.lock:
            if self.driver: 
                return # Already running

            opts = Options()
            opts.add_argument("--headless")
            opts.add_argument("--disable-gpu")
            opts.add_argument("--disable-dev-shm-usage") # Critical for memory management
            opts.add_argument("--hide-scrollbars")
            opts.add_argument("--log-level=3")
            opts.add_argument("--no-sandbox")

            try:
                service = Service(ChromeDriverManager().install())
                self.driver = webdriver.Chrome(service=service, options=opts)
                self.driver.set_page_load_timeout(45) # Hard limit for page loads
                # Update timestamp so watchdog doesn't kill it immediately
                self.last_used_time = time.time() 
            except Exception as e:
                print(f"Driver Init Error: {e}")

    def capture(self, url: str, width: int, height: int, wait_time: int, 
                status_cb: Callable, progress_cb: Callable) -> Optional[Image.Image]:
        
        # Update timestamp to prevent watchdog from killing during capture
        self.last_used_time = time.time()

        # Check/Start Driver
        if not self.driver:
            status_cb("Waking up engine...")
            self.init_driver()
            if not self.driver: return None

        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url

        try:
            # We acquire lock only for browser operations to ensure 
            # watchdog doesn't kill the process while we are using it.
            with self.lock:
                self.driver.set_window_size(width, height)
                
                status_cb(f"Navigating...")
                self.driver.get(url)

                # Smart Wait (DOM)
                WebDriverWait(self.driver, 15).until(
                    lambda d: d.execute_script("return document.readyState") == "complete"
                )

            # Manual Wait (Release lock here so UI doesn't freeze, but keep updating timestamp)
            status_cb(f"Waiting {wait_time}s...")
            steps = wait_time * 10
            for i in range(steps):
                time.sleep(0.1)
                self.last_used_time = time.time() # Keep alive
                progress_cb(((i + 1) / steps) * 100)
            
            with self.lock:
                status_cb("Capturing...")
                png_data = self.driver.get_screenshot_as_png()
                self.last_used_time = time.time() # Reset timer
                return Image.open(io.BytesIO(png_data))

        except Exception as e:
            print(f"Backend Error: {e}")
            return None

    def close(self):
        """Final cleanup."""
        self.running = False # Stop watchdog loop
        with self.lock:
            if self.driver:
                try:
                    self.driver.quit()
                except:
                    pass

# --- FRONTEND UI ---
class StrangerPrintsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("StrangerPrints")
        self.configure(bg="#1E1E1E")
        
        # State
        self.engine = ScreenshotEngine()
        self.current_image = None
        self.preview_opened_once = False 

        # Setup
        self._setup_styles()
        self._build_ui()
        
        # Set 500x600 and Center it
        self._center_window(500, 600)
        
        # Warmup
        threading.Thread(target=self._warmup, daemon=True).start()

        # UI Watchdog Listener (to update status label if engine drops)
        self.after(5000, self._check_engine_status)

    def _center_window(self, w, h):
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        y = max(0, y - 50) 
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def _setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam') 

        bg_color = "#1E1E1E"
        accent_color = "#6C5CE7"
        
        style.configure("TLabel", background=bg_color, foreground="#FFFFFF", font=("Segoe UI", 10))
        style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"), foreground=accent_color)
        style.configure("Status.TLabel", foreground="#AAAAAA", font=("Segoe UI", 9))
        style.configure("TFrame", background=bg_color)
        
        style.configure("TButton", font=("Segoe UI", 9, "bold"), borderwidth=0, background=accent_color, foreground="white")
        style.map("TButton", background=[('active', "#5649C0")])
        
        style.configure("TEntry", fieldbackground="#2D2D2D", foreground="white", insertcolor="white", padding=5)
        style.configure("TCombobox", fieldbackground="#2D2D2D", background="#2D2D2D", foreground="white", arrowcolor="white")
        style.configure("Horizontal.TProgressbar", background=accent_color, troughcolor="#2D2D2D", borderwidth=0)

    def _build_ui(self):
        header_frame = ttk.Frame(self)
        header_frame.pack(fill="x", padx=30, pady=(15, 10))
        ttk.Label(header_frame, text="StrangerPrints", style="Header.TLabel").pack()

        controls_frame = ttk.Frame(self)
        controls_frame.pack(fill="x", padx=30, pady=0)

        # URL
        ttk.Label(controls_frame, text="Target URL").pack(anchor="w")
        self.ent_url = ttk.Entry(controls_frame, font=("Segoe UI", 10))
        self.ent_url.pack(fill="x", pady=(2, 10))

        # Settings Row
        settings_row = ttk.Frame(controls_frame)
        settings_row.pack(fill="x", pady=(0, 10))

        # Res
        res_col = ttk.Frame(settings_row)
        res_col.pack(side="left", fill="x", expand=True, padx=(0, 5))
        ttk.Label(res_col, text="Resolution").pack(anchor="w")
        self.res_map = {
            "Full HD (1920x1080)": (1920, 1080),
            "4K UHD (3840x2160)": (3840, 2160),
            "Mobile (375x812)": (375, 812),
            "Instagram (1080x1080)": (1080, 1080)
        }
        self.combo_res = ttk.Combobox(res_col, values=list(self.res_map.keys()), state="readonly")
        self.combo_res.current(0)
        self.combo_res.pack(fill="x", pady=2)

        # Time
        time_col = ttk.Frame(settings_row)
        time_col.pack(side="left", fill="x", expand=True, padx=(5, 0))
        ttk.Label(time_col, text="Wait (s)").pack(anchor="w")
        self.spin_time = tk.Spinbox(time_col, from_=0, to=30, bg="#2D2D2D", fg="white", 
                                    font=("Segoe UI", 9), relief="flat", buttonbackground="#2D2D2D")
        self.spin_time.delete(0, "end")
        self.spin_time.insert(0, 3)
        self.spin_time.pack(fill="x", pady=2, ipady=3)

        # Capture Button
        self.btn_capture = ttk.Button(controls_frame, text="RENDER SCREENSHOT", command=self.start_capture)
        self.btn_capture.pack(fill="x", pady=5, ipady=3)

        # Progress
        self.progress = ttk.Progressbar(controls_frame, mode='determinate', length=100)
        self.progress.pack(fill="x", pady=(0, 5))

        # Preview Area
        self.preview_frame = tk.Frame(controls_frame, bg="#151515", height=150)
        self.preview_frame.pack(fill="x", pady=5)
        self.preview_frame.pack_propagate(False) 

        self.lbl_thumbnail = tk.Label(self.preview_frame, bg="#151515", text="[ No Image ]", fg="#444")
        self.lbl_thumbnail.pack(expand=True, fill="both")

        # Action Buttons
        actions_frame = ttk.Frame(controls_frame)
        actions_frame.pack(fill="x", pady=5)
        
        self.btn_open = ttk.Button(actions_frame, text="Open Full View", command=self.open_full_preview, state="disabled")
        self.btn_open.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        self.btn_save = ttk.Button(actions_frame, text="Save to Disk", command=self.save_file, state="disabled")
        self.btn_save.pack(side="left", fill="x", expand=True, padx=(5, 0))

        # Status
        self.lbl_status = ttk.Label(controls_frame, text="System Ready", style="Status.TLabel")
        self.lbl_status.pack(pady=5)

        # Footer
        footer_frame = tk.Frame(self, bg="#1E1E1E")
        footer_frame.pack(side="bottom", fill="x", pady=15)
        
        tk.Label(footer_frame, text="Developed by: João V. Coelho | 2025", 
                 bg="#1E1E1E", fg="#666666", font=("Segoe UI", 8)).pack()
        
        link = tk.Label(footer_frame, text="https://github.com/joaovcoelho", 
                        bg="#1E1E1E", fg="#6C5CE7", font=("Segoe UI", 8, "underline"), cursor="hand2")
        link.pack()
        link.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/joaovcoelho"))

    def _warmup(self):
        self.lbl_status.config(text="Initializing Engine...")
        try:
            self.engine.init_driver()
            self.lbl_status.config(text="Ready.")
        except:
            self.lbl_status.config(text="Engine Init Failed.")

    def _check_engine_status(self):
        """Polls to see if engine is asleep."""
        if not self.engine.driver and self.btn_capture['state'] == 'normal':
             self.lbl_status.config(text="Idle (Resources Freed)")
        self.after(2000, self._check_engine_status)

    def start_capture(self):
        url = self.ent_url.get().strip()
        if not url: return

        self.btn_capture.config(state="disabled")
        self.btn_open.config(state="disabled")
        self.btn_save.config(state="disabled")
        self.progress['value'] = 0
        
        res_name = self.combo_res.get()
        w, h = self.res_map[res_name]
        try: wait = int(self.spin_time.get())
        except: wait = 3

        t = threading.Thread(target=self._run_capture, args=(url, w, h, wait))
        t.start()

    def _run_capture(self, url, w, h, wait):
        img = self.engine.capture(
            url, w, h, wait, 
            lambda t: self.lbl_status.config(text=t), 
            lambda v: self.progress.configure(value=v)
        )
        self.after(0, lambda: self._finish_capture(img))

    def _finish_capture(self, image):
        self.btn_capture.config(state="normal")
        self.progress['value'] = 100
        
        if image:
            self.current_image = image
            self.preview_opened_once = False
            self.lbl_status.config(text="Complete.", foreground="#55FF55")
            
            thumb = image.copy()
            thumb.thumbnail((440, 150))
            self.tk_thumb = ImageTk.PhotoImage(thumb)
            self.lbl_thumbnail.config(image=self.tk_thumb, text="")
            
            self.btn_open.config(state="normal")
            self.btn_save.config(state="normal")
        else:
            self.lbl_status.config(text="Failed.", foreground="#FF5555")

    def open_full_preview(self):
        if not self.current_image or self.preview_opened_once: return
        self.current_image.show()
        self.preview_opened_once = True
        self.btn_open.config(state="disabled", text="Opened")

    def save_file(self):
        if not self.current_image: return
        path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if path:
            self.current_image.save(path, optimize=True)
            self.lbl_status.config(text="Saved.")

    def on_close(self):
        self.withdraw()
        threading.Thread(target=self.engine.close).start()
        os._exit(0)

if __name__ == "__main__":
    app = StrangerPrintsApp()
    app.protocol("WM_DELETE_WINDOW", app.on_close)
    app.mainloop()
