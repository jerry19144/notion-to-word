<div align="center">

<img width="409.6" height="409.6" alt="Generated Image September 21, 2025 - 11_52AM" src="https://github.com/user-attachments/assets/71bd57a0-ec62-4f39-982c-de189fd63ccf" />

**Convert your Notion pages to beautifully formatted Word documents**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![UV](https://img.shields.io/badge/UV-Package%20Manager-blueviolet.svg)](https://github.com/astral-sh/uv)
[![Tests](https://img.shields.io/badge/Tests-Passing-green.svg)](#testing)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

*Clean, fast, and reliable conversion from Notion to Word with custom styling*

[✨ Features](#-features) • [🚀 Quick Start](#-quick-start) • [📖 Usage](#-usage) • [🎨 Templates](#-custom-templates) • [🤝 Contributing](#-contributing)

---

</div>

## ✨ Features

- **⚡ Lightning Fast**: Sub-2 second conversion for most pages
- **🎨 Custom Templates**: Use your own Word templates with style mappings
- **🔍 Smart URL Parsing**: Works with any Notion share link format
- **📦 Batch Conversion**: Convert entire databases at once
- **💎 Rich Formatting**: Preserves text styles, colors, and formatting
- **🛡️ Robust Processing**: Handles all Notion block types with graceful fallbacks
- **🚀 Modern Tooling**: Built with UV for 10-100x faster package management
- **📁 Clean Architecture**: Professional Python package following best practices

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+**
- **Notion Integration Token** ([Get yours here](https://www.notion.so/my-integrations))

### Installation

#### Option 1: UV (Recommended - Fast & Modern)

```bash
# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone and setup
git clone https://github.com/tristan-mcinnis/notion-to-word.git
cd notion-to-word
uv sync

# Configure
cp .env.example .env
# Add your NOTION_TOKEN to .env
```

#### Option 2: pip (Traditional)

```bash
git clone https://github.com/tristan-mcinnis/notion-to-word.git
cd notion-to-word
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Configure
cp .env.example .env
# Add your NOTION_TOKEN to .env
```

### Get Your Notion Token

1. Go to [Notion Integrations](https://www.notion.so/my-integrations)
2. Click "New integration" → Name it "Notion to Word"
3. Copy the **Internal Integration Token**
4. Add to `.env`: `NOTION_TOKEN=your_token_here`
5. **Important**: Share your Notion pages with this integration!

## 📖 Usage

### Basic Commands

```bash
# Convert a page
uv run notion-to-word "https://notion.so/your-page-url"

# With auto-open
uv run notion-to-word "https://notion.so/your-page" --open

# Convert database
uv run notion-to-word "https://notion.so/your-database" --database

# Interactive mode
uv run notion-to-word
```

### Make Commands (Development)

```bash
make setup         # Install dependencies
make test          # Run tests
make run           # Interactive mode
make convert URL="https://notion.so/page"
make help          # Show all commands
```

### All Options

```bash
uv run notion-to-word [URL] [OPTIONS]

Options:
  -o, --output PATH      Custom output file path
  -d, --output-dir DIR   Output directory (default: outputs/)
  -t, --template PATH    Word template file
  --no-template          Skip template styling
  --database             Convert all pages in database
  --open                 Open file after conversion
  -v, --verbose          Detailed output
  -h, --help             Show help
```

## 🎨 Custom Templates

### 1. Create Your Template

1. Open **Microsoft Word**
2. Design with custom styles: Title, Heading 1, Heading 2, Normal, etc.
3. Set fonts, colors, spacing to match your brand
4. Save as `templates/my-template.docx`

### 2. Configure Style Mapping

Edit `config/styles.json`:

```json
{
  "templates": {
    "my_template": {
      "name": "My Brand Template",
      "path": "templates/my-template.docx",
      "font": "Aptos",
      "style_mappings": {
        "title": "Title",
        "heading_1": "Heading 1",
        "heading_2": "Heading 2",
        "paragraph": "Normal",
        "quote": "Quote",
        "code": "Code",
        "default": "Normal"
      }
    }
  }
}
```

### 3. Use Your Template

```bash
uv run notion-to-word "URL" --template "templates/my-template.docx"
```

## 📋 Supported Content

| Content Type | Support | Notes |
|--------------|---------|-------|
| **Text & Paragraphs** | ✅ Full | Rich text, colors, formatting |
| **Headings 1-6** | ✅ Full | Mapped to Word styles |
| **Lists** | ✅ Full | Bulleted, numbered, to-do |
| **Code Blocks** | ✅ Full | Syntax highlighting preserved |
| **Quotes** | ✅ Full | Styled and indented |
| **Callouts** | ✅ Full | With emoji and styling |
| **Tables** | ⚠️ Basic | Simple structure |
| **Images** | ⚠️ Basic | Captions and placeholders |

## 🧪 Testing

```bash
# Quick test
make test

# Full test suite
make test-full

# Real conversion test
make test-real
```

**Test Coverage**: Environment setup, URL parsing, API connectivity, document generation, and end-to-end conversion.

## ⚡ Performance

- **Simple pages** (< 50 blocks): **< 2 seconds**
- **Medium pages** (50-200 blocks): **2-5 seconds**
- **Large pages** (200+ blocks): **5-10 seconds**
- **Database conversion**: **~3 seconds per page**

*Performance varies by internet speed and page complexity.*

## 🛠️ Development

### Setup Development Environment

```bash
make setup      # Install with dev dependencies
make test       # Run tests
make format     # Auto-format code
make lint       # Check code quality
```

### Project Structure

```
notion-to-word/
├── notion_to_word/          # Main package
│   ├── cli.py              # Command-line interface
│   ├── converter.py        # Core conversion logic
│   ├── notion_client.py    # Notion API wrapper
│   └── ...                 # Other modules
├── tests/                   # Test suite
├── templates/              # Word templates
├── config/                 # Configuration files
└── outputs/               # Generated documents
```

### Adding Dependencies

```bash
uv add package-name          # Production dependency
uv add --dev package-name    # Development dependency
```

## 🐛 Troubleshooting

<details>
<summary><strong>Common Issues & Solutions</strong></summary>

**❌ "Page not found" or "Unauthorized"**
- Ensure page is shared with your integration
- Check integration has workspace access
- Verify token starts with `ntn_` or `secret_`

**❌ "Template not found"**
- Check template exists in `templates/` directory
- Use `--no-template` to skip styling
- Verify file path is correct

**❌ "Slow conversion"**
- Check internet connection
- Large pages take longer (normal)
- Notion API has rate limits

</details>

### Debug Mode

```bash
uv run notion-to-word "URL" --verbose
```

### Clean Reinstall

```bash
make clean && rm -rf .venv && uv sync
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Make** your changes and test: `make test`
4. **Format** your code: `make format`
5. **Commit** your changes: `git commit -m 'Add amazing feature'`
6. **Push** to branch: `git push origin feature/amazing-feature`
7. **Open** a Pull Request

### Contribution Guidelines

- ✅ Code follows existing style (Black + Ruff)
- ✅ Tests pass (`make test`)
- ✅ Documentation is updated
- ✅ Commits are descriptive

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Built with these amazing tools:

- [**notion-client**](https://github.com/ramnes/notion-sdk-py) - Official Notion SDK
- [**python-docx**](https://python-docx.readthedocs.io/) - Word document generation
- [**UV**](https://github.com/astral-sh/uv) - Lightning-fast Python package manager
- [**python-dotenv**](https://github.com/theskumar/python-dotenv) - Environment management

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

*Not affiliated with Notion. Notion is a trademark of Notion Labs, Inc.*

</div>
