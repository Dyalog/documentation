FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    ripgrep \
    && rm -rf /var/lib/apt/lists/*

# Create working directory
WORKDIR /docs

# Install mkdocs stack from the pinned requirements file (shared with CI)
COPY requirements-docs.txt /requirements-docs.txt
RUN pip install --no-cache-dir -r /requirements-docs.txt

# Utility-script-only dependencies, unrelated to mkdocs — left unpinned
RUN pip install --no-cache-dir \
    aiohttp \
    lxml \
    Pillow \
    watchdog

# Copy utils scripts
COPY utils /utils

# Make utils directory available in PATH
ENV PATH="/utils:${PATH}"

# Default command
CMD ["python", "--version"]