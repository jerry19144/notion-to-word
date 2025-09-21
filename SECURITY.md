# Security Policy

## 🔒 Reporting Security Vulnerabilities

We take security seriously and appreciate your efforts to responsibly disclose security vulnerabilities.

### How to Report

**Please do NOT create public GitHub issues for security vulnerabilities.**

Instead, please:

1. **Email**: Send details to [security@yourproject.com](mailto:security@yourproject.com)
2. **Include**:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Your contact information

### What to Expect

- **Acknowledgment**: Within 48 hours
- **Initial assessment**: Within 1 week
- **Regular updates**: Every week until resolved
- **Public disclosure**: After fix is released (coordinated with you)

## 🛡️ Security Considerations

### Environment Variables

- **Never commit** `.env` files with real tokens
- **Use strong tokens** from Notion integrations
- **Rotate tokens** regularly
- **Limit integration permissions** to minimum required

### Input Validation

- All Notion URLs are validated before processing
- File paths are sanitized to prevent directory traversal
- Template files are validated before loading

### Data Privacy

- **No data storage**: We don't store your Notion content
- **Local processing**: All conversion happens locally
- **Temporary files**: Cleaned up after conversion
- **No telemetry**: No usage data is collected

### Dependencies

- Regular security updates for all dependencies
- Automated vulnerability scanning
- Minimal dependency footprint

## 📋 Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.x.x   | ✅ Yes             |
| < 1.0   | ❌ No              |

## 🔧 Security Best Practices

### For Users

1. **Keep dependencies updated**:
   ```bash
   uv sync --upgrade
   ```

2. **Use environment variables**:
   ```bash
   # Good
   NOTION_TOKEN=your_token_here

   # Bad - never do this
   python script.py --token=your_token_here
   ```

3. **Verify downloads**:
   ```bash
   # Always clone from official repository
   git clone https://github.com/yourusername/notion-to-word.git
   ```

4. **Limit integration permissions**:
   - Only share required Notion pages
   - Use separate integration for this tool
   - Review permissions regularly

### For Developers

1. **Input sanitization**:
   ```python
   # Always validate user inputs
   def validate_url(url: str) -> bool:
       # Validation logic
   ```

2. **Secure file handling**:
   ```python
   # Use safe path operations
   from pathlib import Path
   safe_path = Path(user_input).resolve()
   ```

3. **Error handling**:
   ```python
   # Don't expose sensitive information in errors
   except Exception as e:
       logger.error(f"Internal error: {type(e).__name__}")
       raise UserError("Conversion failed")
   ```

## 🚨 Known Security Considerations

### Notion API Token

- **Scope**: Limited to shared pages only
- **Storage**: Stored locally in `.env` file
- **Transmission**: HTTPS to Notion API only
- **Logging**: Never logged or displayed

### File System Access

- **Read**: Template files in `templates/` directory
- **Write**: Output files in `outputs/` directory
- **No**: System files or other directories

### Network Requests

- **Notion API**: Official API endpoints only
- **No tracking**: No analytics or telemetry
- **HTTPS**: All network communication encrypted

## 📞 Contact

For security concerns:
- **Email**: security@yourproject.com
- **GPG Key**: Available on request
- **Response time**: Within 48 hours

For general questions:
- **GitHub Issues**: For non-security bugs and features
- **Discussions**: For questions and community support

## 🙏 Hall of Fame

We appreciate security researchers who help keep our project safe:

- [Your name here] - Responsible disclosure of [issue type]

*Want to be listed? Report a security vulnerability responsibly!*

---

**Last updated**: December 2024