#!/usr/bin/env bash

set -e

CONTENT_DIR="content"

echo "Scanning $CONTENT_DIR for missing _index.md files..."
echo

# Find all directories under content (except the root content/ itself)
find "$CONTENT_DIR" -type d | while read -r dir; do
    # Skip the top-level content directory itself
    if [ "$dir" = "$CONTENT_DIR" ]; then
        continue
    fi

    INDEX_FILE="$dir/_index.md"

    if [ ! -f "$INDEX_FILE" ]; then
        # Generate a human friendly title from the folder name
        folder_name=$(basename "$dir")
        title=$(echo "$folder_name" | sed -E 's/[-_]+/ /g' | sed 's/\b\(.\)/\u\1/g')

        # Optional: generate weight based on alphabetical order
        weight=$(echo "$folder_name" | tr -cd '[[:alpha:]]' | wc -c)

        echo "Creating: $INDEX_FILE"
        cat > "$INDEX_FILE" <<EOF
---
title: "$title"
weight: $weight
---
EOF
    fi
done

echo
echo "Done! All directories now have _index.md files."

