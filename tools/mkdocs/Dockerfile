FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    git

COPY requirements-docs.txt /requirements-docs.txt
RUN pip install -r /requirements-docs.txt

RUN pip install --force-reinstall click==8.2.1


# Set the working directory
WORKDIR /docs

# Default command to run MkDocs server
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]
