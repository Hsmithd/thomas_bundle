import os
from pathlib import Path

ROOT = Path("content/doc_sample")   # same as your bash version
weight = 10

def title_case_from_dirname(name: str) -> str:
    # "whiskey-banana" → "Whiskey Banana"
    return " ".join(w.capitalize() for w in name.replace("-", " ").split())

print(f"Scanning for README.md under: {ROOT.resolve()}")

# recursively find all README.md files
readme_files = list(ROOT.rglob("README.md"))

for readme in readme_files:
    dir_path = readme.parent
    newfile = dir_path / "_index.md"

    # directory name = title
    dirname = dir_path.name
    title = title_case_from_dirname(dirname)

    print(f"Processing: {readme} → {newfile} (title={title})")

    # read original content
    with open(readme, "r", encoding="utf-8") as f:
        original = f.read()

    # write _index.md with front matter + original content
    front_matter = (
        "---\n"
        f"title: \"{title}\"\n"
        f"linkTitle: \"{title}\"\n"
        f"weight: {weight}\n"
        "---\n\n"
    )

    with open(newfile, "w", encoding="utf-8") as f:
        f.write(front_matter + original)

    # remove old README.md
    readme.unlink()

    weight += 10

print("Done! All README.md files converted to _index.md with front matter.")

