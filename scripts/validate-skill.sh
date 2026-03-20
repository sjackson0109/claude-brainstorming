#!/bin/bash

# Brainstorming Skill Source Validation Script
# Validates the brainstorming skill source for release readiness

set -e

SOURCE_DIR="brainstorming"
SKILL_FILE="brainstorming.skill"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

# Parse command line arguments
GENERATE_SKILL=false
for arg in "$@"; do
    case $arg in
        --generate)
            GENERATE_SKILL=true
            shift
            ;;
    esac
done

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🔍 Brainstorming Skill Source Validation${NC}"
echo "=========================================="

# Change to root directory
cd "$ROOT_DIR"

# Check if source directory exists
echo -n "Checking source directory... "
if [ ! -d "$SOURCE_DIR" ]; then
    echo -e "${RED}✗ FAIL${NC}"
    echo -e "${RED}Error: $SOURCE_DIR directory not found!${NC}"
    exit 1
fi
echo -e "${GREEN}✓ PASS${NC}"

# Check if main skill file exists
echo -n "Checking main skill file... "
MAIN_SKILL_FILE="$SOURCE_DIR/SKILL.md"
if [ ! -f "$MAIN_SKILL_FILE" ]; then
    echo -e "${RED}✗ FAIL${NC}"
    echo -e "${RED}Error: $MAIN_SKILL_FILE not found!${NC}"
    exit 1
fi
echo -e "${GREEN}✓ PASS${NC}"

# Check for references directory content
echo -n "Checking references directory... "
REFERENCES_DIR="$SOURCE_DIR/references"
if [ ! -d "$REFERENCES_DIR" ]; then
    echo -e "${YELLOW}⚠ WARN${NC}"
    echo -e "${YELLOW}Warning: brainstorming/references directory not found${NC}"
else
    REF_COUNT=$(find "$REFERENCES_DIR" -name "*.md" | wc -l)
    if [ "$REF_COUNT" -lt 10 ]; then
        echo -e "${YELLOW}⚠ WARN${NC}"
        echo -e "${YELLOW}Warning: Only $REF_COUNT reference files found (expected 150+)${NC}"
    else
        echo -e "${GREEN}✓ PASS${NC} ($REF_COUNT reference files)"
    fi
fi

# Check for required documentation
echo -n "Checking documentation files... "
MISSING_DOCS=()
for doc in "README.md" "LICENSE.md"; do
    if [ ! -f "$doc" ]; then
        MISSING_DOCS+=("$doc")
    fi
done

if [ ${#MISSING_DOCS[@]} -gt 0 ]; then
    echo -e "${YELLOW}⚠ WARN${NC}"
    echo -e "${YELLOW}Warning: Missing documentation files: ${MISSING_DOCS[*]}${NC}"
else
    echo -e "${GREEN}✓ PASS${NC}"
fi

# Generate skill file if requested
if [ "$GENERATE_SKILL" = true ]; then
    echo -n "Generating skill file... "
    if python .github/scripts/create_skill.py -path "$SOURCE_DIR"; then
        if [ -f "$SKILL_FILE" ]; then
            GENERATED_SIZE=$(stat -f%z "$SKILL_FILE" 2>/dev/null || stat -c%s "$SKILL_FILE" 2>/dev/null)
            echo -e "${GREEN}✓ PASS${NC} ($GENERATED_SIZE bytes)"
        else
            echo -e "${RED}✗ FAIL${NC}"
            echo -e "${RED}Error: Skill file generation failed${NC}"
            exit 1
        fi
    else
        echo -e "${RED}✗ FAIL${NC}"
        echo -e "${RED}Error: Failed to generate skill file${NC}"
        exit 1
    fi
fi

echo ""
echo -e "${BLUE}📊 Validation Summary${NC}"
echo "========================"
echo -e "Source directory: ${GREEN}$SOURCE_DIR${NC}"
echo -e "References: ${GREEN}$REF_COUNT files${NC}"
if [ "$GENERATE_SKILL" = true ] && [ -f "$SKILL_FILE" ]; then
    SKILL_SIZE=$(stat -f%z "$SKILL_FILE" 2>/dev/null || stat -c%s "$SKILL_FILE" 2>/dev/null)
    echo -e "Generated skill file: ${GREEN}$SKILL_SIZE bytes${NC}"
fi
echo -e "Status: ${GREEN}Ready for release${NC}"
echo ""
echo -e "${GREEN}🎉 Validation completed successfully!${NC}"
echo -e "The skill source is ready to be packaged into a release artifact."