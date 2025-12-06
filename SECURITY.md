# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Currently supported versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

We take the security of StrangerPrints seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### Please DO NOT:
- Open a public GitHub issue for security vulnerabilities
- Disclose the vulnerability publicly before it has been addressed

### Please DO:
1. **Email**: Send details to the repository maintainer via GitHub
2. **Include**: 
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

### What to expect:
- **Confirmation**: We'll acknowledge receipt within 48 hours
- **Updates**: We'll keep you informed about our progress
- **Fix**: We'll work on a fix and release it as soon as possible
- **Credit**: We'll credit you in the release notes (unless you prefer to remain anonymous)

## Security Best Practices

When using StrangerPrints:

1. **Keep dependencies updated**: Regularly update Selenium and webdriver-manager
2. **URL validation**: Be cautious when accepting URLs from untrusted sources
3. **File permissions**: Ensure screenshot files are saved with appropriate permissions
4. **Network security**: Be aware that StrangerPrints downloads ChromeDriver on first run

## Known Security Considerations

### ChromeDriver Download
- ChromeDriver is downloaded automatically by webdriver-manager
- Downloads occur over HTTPS
- Files are cached in `~/.wdm/` directory

### Browser Automation
- Uses headless Chrome for security
- No cookies or session data is persisted between runs
- Each screenshot session is isolated

## Dependency Security

We monitor our dependencies for known vulnerabilities:
- Selenium: Browser automation library
- webdriver-manager: ChromeDriver management

## Updates and Patches

Security updates will be released as patch versions and announced in:
- GitHub Security Advisories
- Release notes
- CHANGELOG.md

## Questions?

If you have questions about security that don't involve reporting a vulnerability, feel free to:
- Open a GitHub issue with the `security` label
- Contact the maintainers

Thank you for helping keep StrangerPrints and its users safe!
