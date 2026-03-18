# Dynamic Skill Counting Architecture

## Overview

The brainstorming orchestrator now uses **dynamic skill counting** to eliminate hard-coded skill count references. This architectural improvement provides automatic maintenance and prevents CI/CD failures when skills are added or modified.

## Architecture Benefits

### ✅ **Before (Hard-coded):**
- Manual updates required in 6+ files for each skill change
- Easy to miss update locations causing validation failures  
- CI/CD fragility due to inconsistent references
- Violates DRY principles

### ✅ **After (Dynamic):**
- **Single source of truth**: Skill count computed from actual files
- **Automatic propagation**: All references update automatically
- **CI/CD resilience**: Validation adapts to actual skill count
- **Maintenance-free**: No manual updates required

## Core Components

### 1. `skill_counter.py` - Dynamic Counting Utility
```bash
# Count current skills
python skill_counter.py --count

# List all skills  
python skill_counter.py --list

# Update all files with current count
python skill_counter.py --update

# Validate count consistency
python skill_counter.py --validate
```

### 2. Updated `validate_repository.py`
- Uses dynamic skill counting via `SkillCounter` class
- Flexible minimum threshold (100 skills) instead of hard-coded limit
- Validates README against actual skill count

### 3. Updated CI/CD Workflow
- `.github/workflows/skill-packaging.yml` now uses `skill_counter.py --validate`
- Eliminates complex one-liner Python validation
- ASCII-only output for cross-platform compatibility

## Usage Workflow

### Adding New Skills
1. **Create skill file**: Add `new-skill.md` to `brainstorming/references/`
2. **Update documentation**: `python skill_counter.py --update`
3. **Validate**: `python skill_counter.py --validate`
4. **Commit**: All files automatically reflect new count

### Maintenance
```bash
# Check current state
python skill_counter.py --count

# Update all references if needed
python skill_counter.py --update

# Validate before committing
python validate_repository.py
```

## Dynamic Update Locations

The system automatically updates skill count references in:

- **Main orchestrator**: `brainstorming/SKILL.md` description
- **Documentation**: `docs/index.md`, `docs/user-guide.md`  
- **Completion message**: `brainstorming/references/systems-thinking.md`
- **CI/CD validation**: Workflow validates against actual count

## Implementation Details

### SkillCounter Class
```python
class SkillCounter:
    def count_skills(self) -> int
    def get_skill_list(self) -> List[str] 
    def update_skill_file(self) -> bool
    def update_documentation(self) -> None
    def validate_count_consistency(self) -> Tuple[bool, List[str]]
```

### Pattern Matching
- Uses regex patterns to find and replace skill count references
- Handles variations: "150 skills", "150+ specialised domains", etc.
- Preserves formatting and context

## Migration Benefits

### Before Dynamic Architecture
```bash
# Manual process for adding one skill:
1. Edit brainstorming/SKILL.md description
2. Edit docs/index.md references  
3. Edit docs/user-guide.md references
4. Edit validate_repository.py thresholds
5. Edit workflow validation logic
6. Update README.md if needed
# 6+ files, high error risk
```

### After Dynamic Architecture  
```bash
# Automated process for adding one skill:
1. Add skill file to references/
2. python skill_counter.py --update
# 2 commands, zero error risk
```

## Future Enhancements

- **Template-based documentation**: Use Jinja2 templates for complex docs
- **Git hooks**: Auto-update counts on pre-commit
- **Semantic validation**: Ensure skill content quality
- **Cross-reference validation**: Verify skill links are valid

## Conclusion

This architecture eliminates the maintenance overhead of hard-coded skill counts while providing a robust foundation for scaling the brainstorming system. Future skill additions now require minimal effort and zero risk of validation failures.

The system demonstrates best practices for:
- **Single Source of Truth**: Count computed from actual files
- **Automation**: Manual processes eliminated  
- **Resilience**: CI/CD adapts to changes automatically
- **Maintainability**: Clear separation of concerns