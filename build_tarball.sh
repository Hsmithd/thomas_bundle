#!/usr/bin/env bash
set -euo pipefail

# 1) The folder you receive (raw md/yml tree)
if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <incoming_docs_folder>"
  exit 1
fi

INCOMING="$1"

if [[ ! -d "$INCOMING" ]]; then
  echo "ERROR: $INCOMING is not a directory"
  exit 1
fi

echo "Using incoming docs folder: $INCOMING"

# 2) Your Hugo site root (script location)
SITE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 3) Where in Hugo these docs should be copied
CONTENT_ROOT="$SITE_ROOT/content/docs/imported"

# 4) Reset imported docs
rm -rf "$CONTENT_ROOT"
mkdir -p "$CONTENT_ROOT"

echo "Copying incoming content into Hugo content/docs/imported/"
cp -r "$INCOMING"/* "$CONTENT_ROOT"/

# 5) Run your MD restructuring scripts
cd "$SITE_ROOT"

if [[ -x scripts/fix_docsy.py ]]; then
  python3 scripts/fix_readmes.py
fi

if [[ -x scripts/add_leaf_front_matter.py ]]; then
  python3 scripts/add_leaf_front_matter.py
fi

if [[ -x scripts/reweight_nav_folders_bottom.py ]]; then
  python3 scripts/reweight_nav_folders_bottom.py
fi

# 6) Build Hugo site
hugo --minify --destination public

# 7) Package as tarball
TARBALL_NAME="bundle-$(date +%Y%m%d-%H%M%S).tar.gz"
tar -czf "$TARBALL_NAME" -C public .

echo "Done: $SITE_ROOT/$TARBALL_NAME"

