#!/bin/bash

# Usage: ./script.sh --day <day> --year <year> --root-dir </path/to/root>
# Example: ./script.sh --day day-01 --year 2024 --root-dir .

set -euo pipefail

REPO_DIR="$(git rev-parse --show-toplevel)"

# Load environment variables from .env file
if [ -f "$REPO_DIR/.env" ]; then
    source "$REPO_DIR/.env"
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
        -d|--day)
            DAY="$2"
            shift 2
            ;;
        -y|--year)
            YEAR="$2"
            shift 2
            ;;
        --root-dir)
            ROOT_DIR="$2"
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

URL="https://adventofcode.com/$YEAR/day/$DAY_NUMBER_NO_LEADING_ZEROS/input"

echo "Sending request to '$URL'"

INPUTS_DIR="${ROOT_DIR}/${DAY}/inputs"
mkdir -p "$INPUTS_DIR"

INPUT_DATA=$(curl -sSL -H "Cookie: session=$SESSION" "$URL")
if [[ -z "$INPUT_DATA" ]]; then
    echo "Error: Failed to fetch input data from '$URL'." >&2
    exit 1
fi

for FILENAME in "input1.txt" "input2.txt"; do
    FILE_PATH="$INPUTS_DIR/$FILENAME"
    echo "$INPUT_DATA" > "$FILE_PATH"
    echo "Wrote to $FILE_PATH"
done

touch "${INPUTS_DIR}/test1.txt"
touch "${INPUTS_DIR}/test2.txt"

echo "Successful!!"
