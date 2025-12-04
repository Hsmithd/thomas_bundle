import os
from pathlib import Path

# 👇 Adjust if needed. If your docs live in content/en/docs, change this.
ROOT = Path("content/docs")

def update_weight_in_front_matter(path: Path, new_weight: int):
    """Update or insert weight: in the YAML front matter of a markdown file."""
    text = path.read_text(encoding="utf-8")

    # We assume YAML front matter with --- ... ---
    parts = text.split("---", 2)
    if len(parts) < 3:
        # No recognizable front matter, skip
        print(f"SKIP (no front matter): {path}")
        return

    prefix, fm, body = parts[0], parts[1], parts[2]
    fm_lines = fm.strip("\n").splitlines()

    new_lines = []
    saw_weight = False
    for line in fm_lines:
        if line.lstrip().startswith("weight:"):
            new_lines.append(f"weight: {new_weight}")
            saw_weight = True
        else:
            new_lines.append(line)

    if not saw_weight:
        new_lines.append(f"weight: {new_weight}")

    new_fm = "\n".join(new_lines) + "\n"
    new_text = "---" + new_fm + "---" + body

    path.write_text(new_text, encoding="utf-8")
    print(f"Set weight={new_weight} in {path}")

print(f"Using ROOT = {ROOT.resolve()}")
if not ROOT.exists():
    print("ERROR: ROOT directory does not exist. Adjust ROOT in the script.")
    raise SystemExit(1)

for dirpath, dirnames, filenames in os.walk(ROOT):
    dirpath = Path(dirpath)

    # immediate child markdown files
    md_files = [f for f in filenames if f.endswith(".md")]

    # leaf pages in this folder (not _index.md)
    leaf_pages = sorted(
        [Path(dirpath) / f for f in md_files if f != "_index.md"]
    )

    # child folders (_index.md inside them represents the folder)
    child_dirs = sorted(dirnames)
    child_section_indexes = []
    for d in child_dirs:
        idx = Path(dirpath) / d / "_index.md"
        if idx.exists():
            child_section_indexes.append(idx)

    # nothing to do if no leaf pages and no child folders
    if not leaf_pages and not child_section_indexes:
        continue

    print(f"\n=== Directory: {dirpath} ===")

    # pages first: weights 10,20,30,...
    weight_step = 10
    weight = 10
    for page in leaf_pages:
        update_weight_in_front_matter(page, weight)
        weight += weight_step

    # folders (their _index.md) after pages
    # start after the last page weight
    if leaf_pages:
        folder_weight = weight
    else:
        folder_weight = 10  # no pages, folders can start at 10

    for idx in child_section_indexes:
        update_weight_in_front_matter(idx, folder_weight)
        folder_weight += weight_step

print("\nDone re-weighting pages (pages first, folders at bottom).")

