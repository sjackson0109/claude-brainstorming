import os
import sys
import zipfile
import argparse

parser = argparse.ArgumentParser(description="Package a skill directory as a .skill zip file.")
parser.add_argument("-path", required=True, help="Path to the skill directory to package")
args = parser.parse_args()

source_dir = os.path.abspath(args.path)
base_dir = os.path.dirname(source_dir)
skill_name = os.path.basename(source_dir)
zip_path = os.path.join(base_dir, f"{skill_name}.skill")

EXCLUDE_FILES = {"unused.md"}
EXCLUDE_DIRS = {".git", "__pycache__", ".vscode", "node_modules"}

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(source_dir):
        # Remove excluded directories from the dirs list to prevent os.walk from entering them
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        for file in files:
            if file in EXCLUDE_FILES:
                continue
            abs_path = os.path.join(root, file)
            rel_path = os.path.relpath(abs_path, source_dir).replace("\\", "/")
            zf.write(abs_path, rel_path)
            print(f"  added: {rel_path}")
        
        # Create directory entries in the zip for empty directories
        if not files and not dirs:
            rel_dir = os.path.relpath(root, source_dir).replace("\\", "/")
            if rel_dir != ".":
                zf.writestr(f"{rel_dir}/", "")
                print(f"  added: {rel_dir}/ (empty directory)")

print(f"\nDone: {zip_path}")
