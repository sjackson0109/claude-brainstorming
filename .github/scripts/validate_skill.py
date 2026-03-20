#!/usr/bin/env python3
"""
Validate the packaged brainstorming skill file.
"""
import zipfile
import sys
import os
import argparse

def validate_skill_package(skill_file_path):
    """Validate the contents of a .skill package file."""
    
    if not os.path.exists(skill_file_path):
        print(f"❌ Skill file not found: {skill_file_path}")
        return False
    
    try:
        with zipfile.ZipFile(skill_file_path, 'r') as zf:
            files = zf.namelist()
            
            print(f"[VALIDATE] Validating {skill_file_path}...")
            print(f"   Package contains {len(files)} files")
            
            # Check for main skill file
            if 'SKILL.md' not in files:
                print('[ERROR] SKILL.md not found in package')
                return False
            print('[OK] Main SKILL.md file found')
            
            # Check for references directory structure
            ref_files = [f for f in files if f.startswith('references/') and f.endswith('.md')]
            if len(ref_files) < 130:
                print(f'❌ Expected at least 130 reference files, found {len(ref_files)}')
                return False
            
            print(f'[OK] Found {len(ref_files)} reference skill files')
            
            # Validate some key reference files exist
            key_skills = [
                'references/api-design.md',
                'references/cybersecurity.md',
                'references/user-interface-design.md',
                'references/strategic-planning.md',
                'references/mermaid-diagrams.md'
            ]
            
            missing_key_skills = []
            for skill in key_skills:
                if skill not in files:
                    missing_key_skills.append(skill)
            
            if missing_key_skills:
                print(f'[ERROR] Missing key skill files: {missing_key_skills}')
                return False
            
            print('[OK] Key skill files validated')
            print('[OK] Skill package validation successful')
            return True
            
    except zipfile.BadZipFile:
        print(f'[ERROR] Invalid zip file: {skill_file_path}')
        return False
    except Exception as e:
        print(f'[ERROR] Error validating skill package: {e}')
        return False

def main():
    parser = argparse.ArgumentParser(description="Validate brainstorming skill package")
    parser.add_argument("-file", default="brainstorming.skill", 
                       help="Path to the .skill file to validate")
    args = parser.parse_args()
    
    success = validate_skill_package(args.file)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()