FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create working directory
WORKDIR /docs

# Install Python dependencies for utils scripts
RUN pip install --no-cache-dir \
    mkdocs \
    mkdocs-material \
    mkdocs-monorepo-plugin \
    mkdocs-macros-plugin \
    mkdocs-caption \
    pymdown-extensions \
    ruamel.yaml \
    beautifulsoup4 \
    aiohttp \
    lxml \
    Pillow

# Copy utils scripts
COPY utils /utils

# Make utils directory available in PATH
ENV PATH="/utils:${PATH}"

# Default command
CMD ["python", "--version"]