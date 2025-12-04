# Language Support

This directory contains centralized language-specific configurations that work for any year.

## Current Languages

- **Go** (`languages/go/`) - Go language support
- **Rust** (`languages/rust/`) - Rust language support
- **Python** (`languages/python/`) - Python language support (uses uv)
- **C++** (`languages/cpp/`) - C++ language support
- **Java** (`languages/java/`) - Java language support
- **Kotlin** (`languages/kotlin/`) - Kotlin language support

## Structure

Each language directory contains:
- `justfile` - Language-specific commands (create, run, test, etc.)
- `template/` - Template files for generating new day solutions
- `README.md` - Language-specific documentation

## Adding a New Language

To add support for a new language (e.g., Python):

1. **Create the directory:**
   ```bash
   mkdir -p languages/python/template
   ```

2. **Create templates:**
   Add your template files in `languages/python/template/`
   - Name them with `.tmpl` extension if they need processing
   - Or use cargo-generate style templates

3. **Create a justfile:**
   Create `languages/python/justfile` with these commands:
   ```justfile
   root_dir := justfile_directory() / ".." / ".."
   template_dir := justfile_directory() / "template"
   
   create year day:
     # Your create logic here
   
   run year day part:
     # Your run logic here
   
   test year day part:
     # Your test logic here
   
   test-all year day:
     # Your test-all logic here
   
   get-inputs year day:
     # Your get-inputs logic here
   ```

4. **That's it!** The root justfile will automatically work with your new language:
   ```bash
   just create 2024 python day-01
   just run 2024 python day-01 1
   ```

## Benefits

✅ **No duplication** - Each language defined once, works for all years
✅ **Scalable** - Add 2025, 2026, etc. without any configuration
✅ **Easy to add languages** - Just add a new directory in `languages/`
✅ **Centralized templates** - Update once, affects all years
✅ **Consistent interface** - Same commands work for all languages
