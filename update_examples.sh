#!/bin/bash
set -euo pipefail

NOTEBOOK_PATH="media/Template.ipynb"

ATTACHMENT_PATH="media"
TEMP=$(mktemp -d)

if [ ! -e "$TEMP" ]; then
  >&2 echo "Failed to create temp directory"
  exit 1
fi

trap "exit 1"          HUP INT PIPE QUIT TERM
trap 'rm -rf "$TEMP"'  EXIT

export_notebook() {
  jupyter nbconvert \
    --execute \
    --output-dir="$TEMP" \
    --to markdown \
    "$1"
}

main() {
  export_notebook "$NOTEBOOK_PATH"
	awk '/^## Examples/{print; exit} 1' README.md > "$TEMP/README.md"
  rsync -av --exclude="*.md" "$TEMP/" "$ATTACHMENT_PATH"
  cat "$TEMP/README.md" "$TEMP/Template.md" > "$TEMP/README-update.md"
  awk '{gsub(/Template_files\//, "media/Template_files/"); print}' "$TEMP/README-update.md" > README.md
}

main "$@"
