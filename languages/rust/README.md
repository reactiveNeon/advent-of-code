# Rust Language Support

This directory contains the centralized Rust language configuration for all years.

## Structure

- `justfile` - Rust-specific commands that work for any year
- `template/` - Template files used to generate new day solutions (via cargo-generate)

## Template Files

Uses `cargo-generate` to create new days from the template directory.

## How It Works

When you run `just create 2024 rust day-01` from the root:
1. The root justfile calls this directory's justfile
2. This justfile uses cargo-generate with the template
3. A new Cargo project is created in `2024/rust/day-01/`

This approach allows the same templates and logic to be reused for any year!

## Prerequisites

```bash
cargo install cargo-generate
```
