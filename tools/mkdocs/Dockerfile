FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    git

RUN pip install \
    mkdocs-material \
    mkdocs-macros-plugin \
    mkdocs-monorepo-plugin \
    mkdocs-site-urls \
    mkdocs-caption \
    markdown-tables-extended

# Set the working directory
WORKDIR /docs

# Default command to run MkDocs server
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]