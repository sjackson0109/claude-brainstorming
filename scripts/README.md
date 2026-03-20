# Scripts Directory

This directory contains utility scripts for managing and validating the Brainstorming Skill project.

## Available Scripts

### `validate-skill.sh`
**Platform:** Linux/macOS/WSL  
**Purpose:** Validates the brainstorming skill source for release readiness

**Usage:**
```bash
# Validate source only
./scripts/validate-skill.sh

# Validate and generate skill file
./scripts/validate-skill.sh --generate
```

**What it checks:**
- ✅ Source directory exists (`brainstorming/`)
- ✅ Main skill file exists (`brainstorming/SKILL.md`)
- ✅ References directory exists and has content
- ✅ Required documentation files present
- ✅ Optionally generates `.skill` file for testing

### `validate-skill.ps1`
**Platform:** Windows PowerShell  
**Purpose:** Same validation as the bash script, but for Windows environments

**Usage:**
```powershell
# Validate source only
.\scripts\validate-skill.ps1

# Validate and generate skill file
.\scripts\validate-skill.ps1 -GenerateSkill

# Enable verbose output
.\scripts\validate-skill.ps1 -Verbose -GenerateSkill
```

**Parameters:**
- `-GenerateSkill`: Generate the `.skill` file after validation
- `-Verbose`: Enable verbose output

## Build Process

The `.skill` file is now a **build artifact** that should NOT be committed to the repository. Instead:

1. **Source files** in `brainstorming/` directory are committed
2. **CI/CD pipeline** generates the `.skill` file using `create_skill.py` 
3. **Release artifacts** contain the generated `.skill` file

This follows CI/CD best practices by separating source code from build artifacts.

## CI/CD Integration

These validation scripts are integrated into the GitHub Actions workflows:

- **`/.github/workflows/release.yml`**: Automatic release creation with skill generation
- **`/.github/workflows/manual-release.yml`**: Manual release creation with version tagging

Both workflows now:
1. Generate the `.skill` file from source
2. Validate the generated file  
3. Package it into release artifacts

## Local Development

### Source Validation
```bash
# Linux/macOS
./scripts/validate-skill.sh

# Windows  
.\scripts\validate-skill.ps1
```

### Testing Skill Generation
```bash
# Linux/macOS
./scripts/validate-skill.sh --generate

# Windows
.\scripts\validate-skill.ps1 -GenerateSkill
```

### Manual Skill Generation
```bash
# From project root
python .github/scripts/create_skill.py -path brainstorming
```

## File Structure

```
brainstorming/
├── .github/
│   └── scripts/
│       └── create_skill.py    # Generates .skill from source
├── brainstorming/             # SOURCE: Skill content
│   ├── SKILL.md              # Main skill file
│   └── references/           # Reference skills
├── scripts/                  # Validation scripts
└── brainstorming.skill       # GENERATED: Build artifact (gitignored)
```

## Exit Codes

- **0**: Validation passed successfully
- **1**: Validation failed (blocking errors found)

Warnings will not cause script failure but should be reviewed before release.

## Contributing

When adding new validation checks:

1. Update both bash and PowerShell scripts
2. Test on respective platforms
3. Update this README with new validation criteria
4. Consider impact on CI/CD skill generation workflow