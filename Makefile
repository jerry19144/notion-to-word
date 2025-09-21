# Makefile for Notion to Word Converter with UV

.PHONY: help setup dev test test-full convert lint format clean run

# Default target
help:
	@echo "Notion to Word Converter - UV Commands"
	@echo "======================================"
	@echo ""
	@echo "Setup & Installation:"
	@echo "  make setup     - Install UV and sync dependencies"
	@echo "  make dev       - Install development dependencies"
	@echo ""
	@echo "Testing:"
	@echo "  make test      - Run automated tests"
	@echo "  make test-full - Run comprehensive test suite"
	@echo "  make test-real - Run real conversion test"
	@echo ""
	@echo "Usage:"
	@echo "  make run       - Run interactive converter"
	@echo "  make convert URL=<url> - Convert a specific page"
	@echo ""
	@echo "Development:"
	@echo "  make lint      - Run code linters"
	@echo "  make format    - Auto-format code"
	@echo "  make clean     - Clean cache files"
	@echo ""
	@echo "Examples:"
	@echo "  make convert URL=\"https://notion.so/page-id\""
	@echo "  make test"

# Install UV if not present, then sync
setup:
	@command -v uv >/dev/null 2>&1 || { \
		echo "Installing UV..."; \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
	}
	@echo "Syncing dependencies with UV..."
	@uv sync
	@echo "✓ Setup complete!"

# Install dev dependencies
dev:
	@echo "Installing development dependencies..."
	@uv sync --all-extras
	@echo "✓ Development environment ready!"

# Run automated tests
test:
	@echo "Running automated tests..."
	@uv run python tests/run_tests.py

# Run full test suite
test-full:
	@echo "Running comprehensive test suite..."
	@uv run python tests/test_suite.py

# Run real conversion test
test-real:
	@echo "Running real conversion test..."
	@uv run python tests/test_conversion.py

# Run interactive mode
run:
	@uv run notion-to-word

# Convert a specific URL
convert:
	@if [ -z "$(URL)" ]; then \
		echo "Error: Please provide a URL"; \
		echo "Usage: make convert URL=\"https://notion.so/your-page\""; \
		exit 1; \
	fi
	@uv run notion-to-word "$(URL)" --open

# Run linters
lint:
	@echo "Running linters..."
	@uv run ruff check . || true
	@uv run black --check . || true

# Format code
format:
	@echo "Formatting code..."
	@uv run black .
	@uv run ruff check --fix .
	@echo "✓ Code formatted!"

# Clean cache files
clean:
	@echo "Cleaning cache files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@rm -rf .pytest_cache .coverage .ruff_cache 2>/dev/null || true
	@rm -rf uv.lock 2>/dev/null || true
	@echo "✓ Cleanup complete!"

# Quick install and test
quick-start: setup test
	@echo "✓ Quick start complete! Try: make run"