import os
from pathlib import Path

# 👇 IMPORTANT: this matches your setup (/content/docs)
ROOT = Path("content/docs")  # change to "content/en/docs" ONLY if you have that

def title_case_from_filename(name: str) -> str:
    # "foxtrot-bravo.md" -> "Foxtrot Bravo"
    name = name.rsplit(".", 1)[0]
    return " ".join(w.capitalize() for w in name.replace("-", " ").split())

print(f"Using ROOT = {ROOT.resolve()}")
if not ROOT.exists():
    print("ERROR: ROOT directory does not exist. Check the path in the script.")
    raise SystemExit(1)

for dirpath, dirnames, filenames in os.walk(ROOT):
    dirpath = Path(dirpath)
    # give each directory its own weight counter
    weight = 10

    # sort for deterministic ordering
    filenames = sorted(filenames)

    for fname in filenames:
        if not fname.endswith(".md"):
            continue
        if fname == "_index.md":
            # skip section index files
            continue

        fpath = dirpath / fname

        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        stripped = content.lstrip()

        if stripped.startswith("---"):
            print(f"SKIP (already has front matter): {fpath}")
            continue

        title = title_case_from_filename(fname)

        front_matter = f"""---
title: "{title}"
linkTitle: "{title}"
weight: {weight}
---

"""

        print(f"ADDING front matter to: {fpath} (title={title}, weight={weight})")

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(front_matter + content)

        weight += 10

print("Done processing leaf pages.")

