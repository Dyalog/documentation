#!/bin/bash
set -e

# Copy source files from read-only mount to writable working directory
echo "================================================================"
echo "[$(date '+%H:%M:%S')] Copying source files from /docs-source to /docs..."
echo "================================================================"
rsync -a --exclude='.git' --exclude='site' --exclude='20.0' --exclude='latest' --exclude='versions.json' /docs-source/ /docs/
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

# Build first, THEN start nginx (so mike doesn't conflict with site directory)
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

# Create the site directory that mike expects
mkdir -p /docs/site
echo "[$(date '+%H:%M:%S')] Created /docs/site directory"
ls -la /docs/site

# Build using mike - it will create the gh-pages branch
echo "[$(date '+%H:%M:%S')] Starting mike deploy..."
mike deploy 20.0

END_TIME=$(date +%s)
ELAPSED=$((END_TIME - START_TIME))

echo ""
echo "================================================================"
echo "[$(date '+%H:%M:%S')] Build complete in ${ELAPSED} seconds!"
echo "================================================================"

# Mike built to /docs/site but that's just the flat structure
# We need to replace it with the gh-pages content (which has the version structure)
echo "[$(date '+%H:%M:%S')] Extracting gh-pages content for serving..."
rm -rf /docs/site
mkdir -p /docs/site

# Export the gh-pages branch content (which has 20.0/ directory structure)
git archive gh-pages | tar -x -C /docs/site

echo "[$(date '+%H:%M:%S')] Documentation prepared"
ls -la /docs/site/

# Start nginx now that the site is ready
echo "[$(date '+%H:%M:%S')] Starting nginx..."
nginx

echo "================================================================"
echo "[$(date '+%H:%M:%S')] Documentation is now live at http://localhost:8080"
echo "================================================================"

# Keep the container running by tailing the access log
echo "[$(date '+%H:%M:%S')] Tailing nginx access logs..."
tail -f /var/log/nginx/access.log
