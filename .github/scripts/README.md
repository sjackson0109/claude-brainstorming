# GitHub Scripts Directory

This directory contains Python utility scripts for managing and automating tasks related to the Brainstorming Skill project.

## Python Scripts

### `create_skill.py`
**Purpose:** Skill creation and management utility
- Creates new skill files with proper structure
- Validates skill format and content
- Helps maintain consistency across skill definitions

### `skill_counter.py`  
**Purpose:** Skill inventory and counting utility
- Counts total number of skills in the project
- Validates skill file structure and naming
- Generates skill statistics and reports

### `validate_repository.py`
**Purpose:** Repository structure validation
- Validates overall project structure and organization
- Checks for required files and directories
- Ensures repository meets quality standards

### `validate_skill.py`
**Purpose:** Individual skill file validation  
- Validates individual skill file format and content
- Checks skill metadata and structure
- Ensures skills meet quality requirements

## Usage

These scripts are designed to be run from the project root directory:

```bash
# From project root (brainstorming/)
python .github/scripts/create_skill.py
python .github/scripts/skill_counter.py  
python .github/scripts/validate_repository.py
python .github/scripts/validate_skill.py
```

## CI/CD Integration

These scripts may be used by GitHub Actions workflows for:
- Automated validation during pull requests
- Release artifact preparation
- Quality assurance checks
- Project maintenance tasks

## Related Files

- **Shell/PowerShell Scripts**: See [`/scripts/`](../../scripts/) for cross-platform validation scripts
- **Workflows**: See [`/workflows/`](../workflows/) for GitHub Actions automation

## Contributing

When modifying these scripts:
1. Maintain backward compatibility where possible
2. Update this documentation
3. Test scripts locally before committing
4. Consider impact on CI/CD workflows