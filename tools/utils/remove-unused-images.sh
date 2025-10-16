#!/usr/bin/env bash

# remove-unused-images.sh
# Process validate_images.py output and remove unreferenced images
# Usage: ./remove-unused-images.sh <yaml-file> [--execute]
#
# By default, this script simulates deletion (dry-run mode).
# Use --execute flag to actually delete files.

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Ensure script is run from tools/ directory
if [ ! -d "utils" ] || [ ! -f "utils/remove-unused-images.sh" ]; then
    echo -e "${RED}Error: This script must be run from the tools/ directory${NC}"
    echo "Please cd to tools/ and run: ./utils/remove-unused-images.sh"
    exit 1
fi

# Repository root is parent of tools/
REPO_ROOT="$(cd .. && pwd)"

# Function to display usage
usage() {
    echo "Usage: $0 <yaml-file> [--execute]"
    echo ""
    echo "Note: This script must be run from the tools/ directory"
    echo ""
    echo "Arguments:"
    echo "  <yaml-file>  Path to YAML file from validate_images.py"
    echo "  --execute    Actually delete files (default is dry-run)"
    echo ""
    echo "Examples:"
    echo "  $0 broken_images4.yaml           # Dry-run (simulation)"
    echo "  $0 broken_images4.yaml --execute # Actually delete files"
    exit 1
}

# Check arguments
if [ $# -lt 1 ]; then
    usage
fi

YAML_FILE="$1"
DRY_RUN=true

# Check for --execute flag
if [ $# -eq 2 ]; then
    if [ "$2" == "--execute" ]; then
        DRY_RUN=false
    else
        echo -e "${RED}Error: Unknown argument '$2'${NC}"
        usage
    fi
fi

# Check if YAML file exists
if [ ! -f "$YAML_FILE" ]; then
    echo -e "${RED}Error: File '$YAML_FILE' not found${NC}"
    exit 1
fi

# Display mode
if [ "$DRY_RUN" = true ]; then
    echo -e "${YELLOW}Running in DRY-RUN mode (simulation only)${NC}"
    echo -e "${YELLOW}No files will be deleted. Use --execute to actually delete files.${NC}"
    echo ""
else
    echo -e "${RED}Running in EXECUTE mode${NC}"
    echo -e "${RED}Files WILL be deleted!${NC}"
    echo ""
    read -p "Are you sure you want to continue? (yes/no): " confirm
    if [ "$confirm" != "yes" ]; then
        echo "Aborted."
        exit 0
    fi
    echo ""
fi

# Extract unreferenced images from YAML
# The unreferenced_images section starts after "unreferenced_images:" and contains lines starting with "- "
unreferenced_images=$(awk '
    /^unreferenced_images:/ { in_section=1; next }
    in_section && /^[a-z_]+:/ { exit }
    in_section && /^- / {
        sub(/^- /, "");
        print
    }
' "$YAML_FILE")

# Check if we found any images
if [ -z "$unreferenced_images" ]; then
    echo -e "${GREEN}No unreferenced images found in $YAML_FILE${NC}"
    exit 0
fi

# Count images
image_count=$(echo "$unreferenced_images" | wc -l | tr -d ' ')
echo -e "Found ${YELLOW}$image_count${NC} unreferenced images"
echo ""

# Process each image
deleted_count=0
not_found_count=0

while IFS= read -r image_path; do
    # Skip empty lines
    [ -z "$image_path" ] && continue

    # Construct full path relative to repository root
    full_path="$REPO_ROOT/$image_path"

    if [ -f "$full_path" ]; then
        if [ "$DRY_RUN" = true ]; then
            echo -e "${YELLOW}[SIMULATE]${NC} git rm \"$image_path\""
        else
            # Use git rm to remove file from both filesystem and git index
            # Change to repo root to use relative paths with git
            (cd "$REPO_ROOT" && git rm "$image_path")
            echo -e "${GREEN}[DELETED]${NC} $image_path"
        fi
        ((deleted_count++))
    else
        echo -e "${RED}[NOT FOUND]${NC} $image_path"
        ((not_found_count++))
    fi
done <<< "$unreferenced_images"

echo ""
echo "Summary:"
echo "--------"
echo "Total unreferenced images: $image_count"
if [ "$DRY_RUN" = true ]; then
    echo -e "${YELLOW}Would delete: $deleted_count${NC}"
else
    echo -e "${GREEN}Deleted: $deleted_count${NC}"
fi

if [ $not_found_count -gt 0 ]; then
    echo -e "${RED}Not found: $not_found_count${NC}"
fi

echo ""
if [ "$DRY_RUN" = true ]; then
    echo -e "${YELLOW}This was a dry-run. To actually delete files, run:${NC}"
    echo -e "${YELLOW}  $0 $YAML_FILE --execute${NC}"
else
    echo -e "${GREEN}Files have been removed and changes are staged in git.${NC}"
    echo -e "${GREEN}Review with 'git status' and commit when ready.${NC}"
fi
