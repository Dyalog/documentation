# Build and serve MkDocs site with nginx
# The site is built at runtime when the container starts, not at image build time

FROM python:3.11-slim

# Create working directory for builds (container-only)
WORKDIR /docs

# Install MkDocs, nginx, git, and required plugins
RUN apt-get update && apt-get install -y --no-install-recommends \
    nginx \
    git \
    rsync \
    && rm -rf /var/lib/apt/lists/* \
    && rm -f /etc/nginx/conf.d/default.conf

COPY tools/requirements-docs.txt /requirements-docs.txt
RUN pip install --no-cache-dir -r /requirements-docs.txt

# Extras not referenced in mkdocs.yml — left unpinned pending a follow-up
# that confirms whether they're still needed.
RUN pip install --no-cache-dir \
    markdown-include \
    mkdocs-git-revision-date-localized-plugin

# Copy nginx configuration
COPY tools/nginx/nginx.conf /etc/nginx/nginx.conf

# Create startup script
COPY tools/nginx/start.sh /start.sh
RUN chmod +x /start.sh

# Expose port 8080
EXPOSE 8080

# Build site and start nginx on container start
# Source will be mounted read-only at /docs-source at runtime
# All builds happen in /docs (container-only)
CMD ["/start.sh"]
