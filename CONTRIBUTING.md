# Contributing to Notion to Word

Thanks for your interest in contributing! This guide will help you get started.

## 🚀 Quick Start

1. **Fork** this repository
2. **Clone** your fork locally
3. **Setup** development environment
4. **Make** your changes
5. **Test** thoroughly
6. **Submit** a pull request

## 🛠️ Development Setup

### Prerequisites

- Python 3.10+
- UV package manager (recommended) or pip
- Git

### Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/notion-to-word.git
cd notion-to-word

# Install dependencies
make setup  # or: uv sync

# Run tests to verify setup
make test
```

## 🧪 Testing

We use comprehensive testing to ensure quality:

```bash
# Run all tests
make test

# Run specific test suites
make test-full     # Interactive comprehensive tests
make test-real     # Real conversion tests

# Run with coverage
uv run pytest --cov=notion_to_word
```

### Test Requirements

- ✅ All existing tests must pass
- ✅ New features should include tests
- ✅ Test coverage should not decrease
- ✅ Tests should run in under 30 seconds

## 📝 Code Style

We use automated formatting and linting:

```bash
# Format code
make format

# Check code quality
make lint

# Fix common issues
uv run ruff check --fix .
```

### Style Requirements

- **Black** for code formatting
- **Ruff** for linting and import sorting
- **Type hints** for new functions
- **Docstrings** for public APIs
- **Clear variable names**

## 🎯 What to Contribute

### 🐛 Bug Fixes

- Look for issues labeled `bug`
- Include reproduction steps in your PR
- Add tests that verify the fix

### ✨ New Features

- Check existing issues and discussions first
- Open an issue to discuss large changes
- Follow existing patterns and conventions
- Update documentation

### 📚 Documentation

- Fix typos or unclear explanations
- Add examples and use cases
- Improve setup instructions
- Update API documentation

### 🧪 Tests

- Improve test coverage
- Add edge case testing
- Performance benchmarks
- Integration tests

## 📋 Pull Request Process

### Before Submitting

1. **Rebase** your branch on latest main
2. **Test** all functionality: `make test`
3. **Format** code: `make format`
4. **Check** style: `make lint`
5. **Update** documentation if needed

### PR Requirements

- **Clear title** describing the change
- **Detailed description** with context
- **Linked issues** if applicable
- **Screenshots** for UI changes
- **Test results** showing all pass

### PR Template

```markdown
## Summary
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing
- [ ] All tests pass locally
- [ ] Added tests for new functionality
- [ ] Manual testing completed

## Checklist
- [ ] Code follows project style
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or marked as such)
```

## 🔧 Development Guidelines

### Code Organization

```
notion_to_word/
├── cli.py              # Command-line interface
├── converter.py        # Main conversion logic
├── notion_client.py    # Notion API wrapper
├── word_formatter.py   # Word document formatting
├── block_processor.py  # Block type processing
└── config.py          # Configuration management
```

### Adding New Block Types

1. Add handler in `block_processor.py`
2. Update style mappings in `config/styles.json`
3. Add tests in `tests/`
4. Update supported blocks in README

### Error Handling

- Use descriptive error messages
- Handle API rate limits gracefully
- Provide helpful troubleshooting tips
- Log errors appropriately

### Performance Considerations

- Keep conversion under 10 seconds for typical pages
- Minimize API calls where possible
- Use efficient data structures
- Profile performance-critical code

## 🏷️ Commit Convention

Use clear, descriptive commit messages:

```bash
# Good examples
git commit -m "fix: handle empty pages gracefully"
git commit -m "feat: add support for table borders"
git commit -m "docs: update installation instructions"
git commit -m "test: add edge cases for URL parsing"

# Prefixes
feat:     New feature
fix:      Bug fix
docs:     Documentation
test:     Testing
refactor: Code refactoring
perf:     Performance improvement
style:    Code style changes
```

## 🤝 Community Guidelines

### Be Respectful

- Use welcoming and inclusive language
- Respect differing viewpoints
- Accept constructive criticism gracefully
- Focus on what's best for the community

### Getting Help

- **Issues**: For bugs and feature requests
- **Discussions**: For questions and ideas
- **Code Review**: Constructive feedback welcome

### Recognition

Contributors are recognized in:
- CONTRIBUTORS.md file
- Release notes for significant contributions
- GitHub contributor statistics

## 📋 Issue Guidelines

### Bug Reports

```markdown
**Describe the bug**
Clear description of the issue

**To Reproduce**
1. Steps to reproduce
2. Expected behavior
3. Actual behavior

**Environment**
- OS: [e.g. macOS 13.0]
- Python: [e.g. 3.11.0]
- Version: [e.g. 1.0.0]

**Additional context**
Screenshots, logs, etc.
```

### Feature Requests

```markdown
**Feature Description**
Clear description of the proposed feature

**Use Case**
Why would this be useful?

**Proposed Solution**
How should this work?

**Alternatives Considered**
Other approaches you've thought about
```

## 🎉 Recognition

We appreciate all contributions! Contributors will be:

- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Invited to provide input on project direction

## ❓ Questions?

- Open a [Discussion](https://github.com/yourusername/notion-to-word/discussions)
- Check existing [Issues](https://github.com/yourusername/notion-to-word/issues)
- Review this contributing guide

Thank you for contributing to Notion to Word! 🚀