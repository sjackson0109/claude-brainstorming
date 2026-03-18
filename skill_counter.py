#!/usr/bin/env python3
"""
Dynamic skill counting utility for the brainstorming orchestrator.
Eliminates hard-coded skill count references.
"""
import os
import sys
import re
from pathlib import Path
from typing import Dict, List, Tuple

class SkillCounter:
    """Utility class for dynamic skill counting and content generation."""
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.references_dir = self.base_path / "brainstorming" / "references"
        
    def count_skills(self) -> int:
        """Count the number of skill files in the references directory."""
        if not self.references_dir.exists():
            return 0
        
        skill_files = list(self.references_dir.glob("*.md"))
        return len(skill_files)
    
    def get_skill_list(self) -> List[str]:
        """Get a list of all skill names (without .md extension)."""
        if not self.references_dir.exists():
            return []
        
        skill_files = list(self.references_dir.glob("*.md"))
        return [f.stem for f in skill_files]
    
    def generate_skill_description(self) -> str:
        """Generate the dynamic skill description for SKILL.md."""
        count = self.count_skills()
        return f"Intelligent brainstorming orchestrator that automatically routes to specialised domain expertise. Activated by any brainstorming request - analyses the context and automatically invokes relevant sub-skills from {count} specialised domains including technical, business, design, strategy, and innovation areas."
    
    def generate_doc_content(self, template: str) -> str:
        """Replace placeholders in documentation templates."""
        count = self.count_skills()
        content = template
        content = content.replace("{{SKILL_COUNT}}", str(count))
        content = content.replace("{{SKILL_COUNT_PLUS}}", f"{count}+")
        return content
    
    def update_skill_file(self):
        """Update the main SKILL.md file with dynamic count."""
        skill_file = self.base_path / "brainstorming" / "SKILL.md"
        if not skill_file.exists():
            print(f"[ERROR] Main skill file not found: {skill_file}")
            return False
        
        with open(skill_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update the description in the frontmatter
        new_description = self.generate_skill_description()
        pattern = r'description:\s*"[^"]*"'
        replacement = f'description: "{new_description}"'
        content = re.sub(pattern, replacement, content)
        
        # Update skill count references in the content
        count = self.count_skills()
        content = re.sub(r'\b\d+\s+specialised\s+domains\b', f'{count} specialised domains', content)
        content = re.sub(r'\b\d+\s+reference\s+skills\b', f'{count} reference skills', content)
        
        with open(skill_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"[OK] Updated {skill_file} with dynamic count: {count}")
        return True
    
    def update_documentation(self):
        """Update all documentation files with dynamic counts."""
        docs_files = [
            ("docs/index.md", [
                (r'\b\d+\+?\s+specialised\s+domains\b', f'{self.count_skills()}+ specialised domains'),
                (r'#\s+\d+\+?\s+specialised\s+domain\s+skills', f'# {self.count_skills()}+ specialised domain skills')
            ]),
            ("docs/user-guide.md", [
                (r'\b\d+\+?\s+specialised\s+domain\s+expertise\s+reference\s+files\b', 
                 f'{self.count_skills()}+ specialised domain expertise reference files'),
                (r'\b\d+\+?\s+specialised\s+domain\s+expertise\s+areas\b',
                 f'{self.count_skills()}+ specialised domain expertise areas')
            ]),
            ("brainstorming/references/systems-thinking.md", [
                (r'all\s+\d+\s+comprehensive\s+brainstorming\s+skills',
                 f'all {self.count_skills()} comprehensive brainstorming skills')
            ])
        ]
        
        for file_path, replacements in docs_files:
            full_path = self.base_path / file_path
            if not full_path.exists():
                print(f"[WARN] Documentation file not found: {full_path}")
                continue
            
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            modified = False
            for pattern, replacement in replacements:
                if re.search(pattern, content):
                    content = re.sub(pattern, replacement, content)
                    modified = True
            
            if modified:
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"[OK] Updated {full_path}")
    
    def validate_count_consistency(self) -> Tuple[bool, List[str]]:
        """Check if all skill count references are consistent."""
        count = self.count_skills()
        errors = []
        
        # Check main skill file
        skill_file = self.base_path / "brainstorming" / "SKILL.md"
        if skill_file.exists():
            with open(skill_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract count from description
            desc_match = re.search(r'from\s+(\d+)\s+specialised\s+domains', content)
            if desc_match and int(desc_match.group(1)) != count:
                errors.append(f"SKILL.md description has {desc_match.group(1)}, expected {count}")
        
        # Check README
        readme_file = self.base_path / "README.md"
        if readme_file.exists():
            with open(readme_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if not re.search(rf'\b{count}\s+(skills|specialised)', content):
                errors.append(f"README.md doesn't reference {count} skills")
        
        return len(errors) == 0, errors

def main():
    """Main CLI interface for the skill counter."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Dynamic skill counting utility")
    parser.add_argument("--count", action="store_true", help="Display skill count")
    parser.add_argument("--list", action="store_true", help="List all skills")
    parser.add_argument("--update", action="store_true", help="Update files with dynamic counts")
    parser.add_argument("--validate", action="store_true", help="Validate count consistency")
    parser.add_argument("--path", default=".", help="Base path to brainstorming directory")
    
    args = parser.parse_args()
    
    counter = SkillCounter(args.path)
    
    if args.count:
        print(f"Skill count: {counter.count_skills()}")
    
    if args.list:
        skills = counter.get_skill_list()
        print(f"Found {len(skills)} skills:")
        for skill in sorted(skills):
            print(f"  - {skill}")
    
    if args.update:
        print("Updating files with dynamic skill counts...")
        counter.update_skill_file()
        counter.update_documentation()
        print("Update complete!")
    
    if args.validate:
        is_valid, errors = counter.validate_count_consistency()
        if is_valid:
            print(f"[OK] All skill count references are consistent ({counter.count_skills()} skills)")
        else:
            print(f"[ERROR] Found {len(errors)} consistency errors:")
            for error in errors:
                print(f"  - {error}")
            sys.exit(1)
    
    if not any([args.count, args.list, args.update, args.validate]):
        # Default: show count
        print(f"Skill count: {counter.count_skills()}")

if __name__ == "__main__":
    main()