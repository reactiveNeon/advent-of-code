#!/bin/bash

# Usage: ./script.sh --day <day> --cwd </path/to/root>

set -euo pipefail

# Load environment variables from .env file
if [ -f .env ]; then
    source .env
else
    echo "Error: .env file not found." >&2
    exit 1
fi

# Ensure SESSION is set in the environment
if [[ -z "${SESSION:-}" ]]; then
    echo "Error: SESSION environment variable must be set." >&2
    exit 1
fi

while [[ $# -gt 0 ]]; do
    case "$1" in
        --day)
            DAY="$2"
            shift 2
            ;;
        --cwd)
            CWD="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1" >&2
            exit 1
            ;;
    esac
done

DAY_NUMBER="${DAY#day-}"
DAY_NUMBER_NO_LEADING_ZEROS=$(echo "$DAY_NUMBER" | sed 's/^0*//')

URL="https://adventofcode.com/2024/day/$DAY_NUMBER_NO_LEADING_ZEROS/input"

echo "Sending request to '$URL'"

TARGET_DIR="$CWD/$DAY/inputs"
mkdir -p "$TARGET_DIR"

INPUT_DATA=$(curl -sSL -H "Cookie: session=$SESSION" "$URL")
if [[ -z "$INPUT_DATA" ]]; then
    echo "Error: Failed to fetch input data from '$URL'." >&2
    exit 1
fi

for FILENAME in "1.txt" "2.txt"; do
    FILE_PATH="$TARGET_DIR/$FILENAME"
    echo "$INPUT_DATA" > "$FILE_PATH"
    echo "Wrote to $FILE_PATH"
done

echo "Successful!!"
