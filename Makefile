SHELL := bash
.DEFAULT_GOAL := help

.PHONY: install
install: ## Create the virtual environment with all dependency groups
	@uv sync

.PHONY: lint
lint: ## Lock consistency and ruff
	@uv lock --locked
	@uv run ruff check .
	@uv run ruff format --check .

.PHONY: test
test: ## Tests with coverage
	@uv run pytest --cov --cov-report=term-missing

.PHONY: verify
verify: lint test ## The one gate: run before reporting any change complete

.PHONY: build
build: ## Build sdist and wheel into dist/
	@uv build

.PHONY: book
book: ## Build the Jupyter Book into book/_build/html
	@uv run --with-requirements book/requirements.txt jupyter-book build book

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-28s\033[0m %s\n", $$1, $$2}'
