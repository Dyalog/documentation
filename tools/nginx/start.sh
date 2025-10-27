#!/bin/bash
set -e

# Create the loading page
create_loading_page() {
    local start_time="$2"
    cat > "$1" <<EOF
<!DOCTYPE html>
<html>
<head>
    <title>Building Documentation</title>
    <meta http-equiv="refresh" content="30">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            padding: 50px;
            background: #f5f5f5;
            color: #333;
            margin: 0;
            line-height: 1.6;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            padding: 40px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            margin: 0 0 30px 0;
            font-size: 2em;
            color: #2c3e50;
        }
        p {
            margin: 15px 0;
        }
        .command {
            background: #2c3e50;
            color: #fff;
            padding: 12px;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Building Documentation</h1>
        <p>The documentation is being built. This might take up to 40 minutes.</p>
        <p>This page will update automatically when the build is complete.</p>
        <p><strong>Build started:</strong> ${start_time}</p>
        <p>To view the Docker logs:</p>
        <div class="command">docker logs -f dyalog-docs-nginx</div>
    </div>
</body>
</html>
EOF
}

# Always start nginx with a loading page
echo "================================================================"
echo "[$(date '+%H:%M:%S')] Starting nginx with loading page"
echo "================================================================"

# Create directory for serving
mkdir -p /docs/site

# Get the current time for the loading page
START_TIMESTAMP="$(date '+%Y-%m-%d %H:%M:%S')"

# Create the loading page
create_loading_page /docs/site/index.html "$START_TIMESTAMP"

# Start nginx
nginx
echo "[$(date '+%H:%M:%S')] Nginx started at http://localhost:8080 (loading page)"

# Build into a staging directory (not the live site directory)
echo "================================================================"
echo "[$(date '+%H:%M:%S')] Starting MkDocs site build in staging area..."
echo "This will take 30-40 minutes for the full documentation set."
echo "================================================================"

START_TIME=$(date +%s)
cd /docs

# Build to a staging directory first
rm -rf /docs/site-staging
mkdocs build --clean --site-dir /docs/site-staging -q

END_TIME=$(date +%s)
ELAPSED=$((END_TIME - START_TIME))

echo ""
echo "================================================================"
echo "[$(date '+%H:%M:%S')] Build complete in ${ELAPSED} seconds!"
echo "================================================================"

# Atomic switch: move the old site out, move the new site in
echo "[$(date '+%H:%M:%S')] Performing atomic switch to new documentation..."

# Backup the loading page (in case we need to revert)
mv /docs/site /docs/site-old

# Move the completed build to the live directory
mv /docs/site-staging /docs/site

# Clean up the old loading page
rm -rf /docs/site-old

# Reload nginx to ensure it picks up any new files
nginx -s reload

echo "================================================================"
echo "[$(date '+%H:%M:%S')] Documentation is now live at http://localhost:8080"
echo "================================================================"

# Keep the container running by tailing the access log
echo "[$(date '+%H:%M:%S')] Tailing nginx access logs..."
tail -f /var/log/nginx/access.log
