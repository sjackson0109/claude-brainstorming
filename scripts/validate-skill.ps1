# Brainstorming Skill Validation Script (PowerShell)
# Validates the brainstorming skill source for release readiness

param(
    [switch]$Verbose = $false,
    [switch]$GenerateSkill = $false
)

$ErrorActionPreference = "Stop"

$SourceDir = "brainstorming"
$SkillFile = "brainstorming.skill"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RootDir = Split-Path -Parent $ScriptDir

# Helper functions for colored output
function Write-Success { 
    param($Message) 
    Write-Host "[PASS] " -ForegroundColor Green -NoNewline
    Write-Host $Message 
}

function Write-Failure { 
    param($Message) 
    Write-Host "[FAIL] " -ForegroundColor Red -NoNewline
    Write-Host $Message 
}

function Write-Warning { 
    param($Message) 
    Write-Host "[WARN] " -ForegroundColor Yellow -NoNewline
    Write-Host $Message 
}

function Write-Info { 
    param($Message) 
    Write-Host $Message -ForegroundColor Blue 
}

Write-Info "Brainstorming Skill Source Validation"
Write-Info "====================================="

# Change to root directory
Set-Location $RootDir

# Check if source directory exists
Write-Host "Checking source directory... " -NoNewline
if (-not (Test-Path $SourceDir)) {
    Write-Host ""
    Write-Failure "Error: $SourceDir directory not found!"
    exit 1
}
Write-Host "PASS" -ForegroundColor Green

# Check if main skill file exists
Write-Host "Checking main skill file... " -NoNewline
$MainSkillFile = "$SourceDir\SKILL.md"
if (-not (Test-Path $MainSkillFile)) {
    Write-Host ""
    Write-Failure "Error: $MainSkillFile not found!"
    exit 1
}
Write-Host "PASS" -ForegroundColor Green

# Check for references directory content
Write-Host "Checking references directory... " -NoNewline
$ReferencesDir = "$SourceDir\references"
if (-not (Test-Path $ReferencesDir)) {
    Write-Host "WARN" -ForegroundColor Yellow
    Write-Warning "brainstorming/references directory not found"
} else {
    $RefCount = (Get-ChildItem $ReferencesDir -Filter "*.md").Count
    if ($RefCount -lt 10) {
        Write-Host "WARN" -ForegroundColor Yellow
        Write-Warning "Only $RefCount reference files found (expected 150+)"
    } else {
        Write-Host "PASS ($RefCount files)" -ForegroundColor Green
    }
}

# Check for required documentation
Write-Host "Checking documentation files... " -NoNewline
$RequiredDocs = @("README.md", "LICENSE.md")
$MissingDocs = @()
foreach ($doc in $RequiredDocs) {
    if (-not (Test-Path $doc)) {
        $MissingDocs += $doc
    }
}

if ($MissingDocs.Count -gt 0) {
    Write-Host "WARN" -ForegroundColor Yellow
    Write-Warning "Missing documentation files: $($MissingDocs -join ', ')"
} else {
    Write-Host "PASS" -ForegroundColor Green
}

# Generate skill file if requested
if ($GenerateSkill) {
    Write-Host "Generating skill file... " -NoNewline
    try {
        & python .github/scripts/create_skill.py -path $SourceDir
        if (Test-Path $SkillFile) {
            $GeneratedSize = (Get-Item $SkillFile).Length
            Write-Host "PASS ($GeneratedSize bytes)" -ForegroundColor Green
        } else {
            Write-Host "FAIL" -ForegroundColor Red
            Write-Failure "Skill file generation failed"
            exit 1
        }
    } catch {
        Write-Host "FAIL" -ForegroundColor Red
        Write-Failure "Error generating skill file: $($_.Exception.Message)"
        exit 1
    }
}

Write-Host ""
Write-Info "Validation Summary"
Write-Info "=================="
Write-Host "Source directory: $SourceDir" -ForegroundColor Green
Write-Host "References count: $RefCount files" -ForegroundColor Green
if ($GenerateSkill -and (Test-Path $SkillFile)) {
    $SkillSize = (Get-Item $SkillFile).Length
    Write-Host "Generated skill file: $SkillSize bytes" -ForegroundColor Green
}
Write-Host "Status: Ready for release" -ForegroundColor Green
Write-Host ""
Write-Host "Validation completed successfully!" -ForegroundColor Green
Write-Host "The skill source is ready to be packaged into a release artifact." -ForegroundColor Green