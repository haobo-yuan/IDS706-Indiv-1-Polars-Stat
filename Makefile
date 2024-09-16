# Makefile

.PHONY: install test format lint all

install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

test:
	pytest -vv --cov=your_module_name --cov-report=term-missing --nbval *.ipynb test_*.py

format:
	black *.py
	nbqa black *.ipynb

lint:
	ruff check *.py
	nbqa ruff *.ipynb

all: install format lint test
