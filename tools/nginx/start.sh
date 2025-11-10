#!/bin/bash
set -e

# Copy source files from read-only mount to writable working directory
echo "================================================================"
echo "[$(date '+%H:%M:%S')] Copying source files from /docs-source to /docs..."
echo "================================================================"
rsync -a --exclude='.git' /docs-source/ /docs/
echo "[$(date '+%H:%M:%S')] Source files copied"

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
    <script>
        // Check if the build is complete by trying to fetch /20.0/
        function checkBuildStatus() {
            fetch('/20.0/')
                .then(response => {
                    if (response.ok) {
                        // Build is complete, redirect to /20.0/
                        window.location.href = '/20.0/';
                    }
                })
                .catch(() => {
                    // Build not ready yet, keep waiting
                });
        }

        // Check every 10 seconds
        setInterval(checkBuildStatus, 10000);

        // Also check immediately on load
        checkBuildStatus();
    </script>
</head>
<body>
    <div class="container">
        <h1>Building Documentation</h1>
        <p>The documentation is being built. This might take up to 40 minutes.</p>
        <p>This page will automatically redirect when the build is complete.</p>
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
echo "[$(date '+%H:%M:%S')] Starting MkDocs site build with mike (version 20.0)..."
echo "This will take 30-40 minutes for the full documentation set."
echo "================================================================"

START_TIME=$(date +%s)
cd /docs

# Initialize git if not already initialized (mike requires git)
if [ ! -d .git ]; then
    git init
    git config user.name "Docker Build"
    git config user.email "build@localhost"
    # Make an initial commit so mike has something to work with
    git add -A
    git commit -m "Initial commit for mike" --allow-empty
fi

# Always set git config (in case .git already existed from mounted volume)
git config user.name "Docker Build"
git config user.email "build@localhost"

# Build using mike EXACTLY as CI does, but WITHOUT --push to keep it local
# This deploys to the local gh-pages branch inside the container only
mike deploy 20.0

# Mike builds to a gh-pages branch, extract it to serve via nginx
rm -rf /docs/site-staging

# Clean up any existing worktrees first
git worktree prune

# Use a simpler approach: checkout gh-pages directly to site-staging
# This avoids the worktree issue with .git paths on macOS
mkdir -p /docs/site-staging
git --work-tree=/docs/site-staging checkout gh-pages -- .

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
