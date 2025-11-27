# Changelog

All notable changes to ArPy will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.0] - 2025-11-27

### Added
- Complete rewrite with modular architecture
- Simple CLI interface with argparse
- 10 encryption methods (marshal, zlib, base64, base32, base16, lambda, bitwise, binhex, charlen, revzlib)
- Auto-detect decryption feature
- Custom color module (no external color dependencies)
- Progress bars with tqdm
- Centralized version management in `main/__init__.py`
- `--list` command to show all available methods
- `--report` command to open GitHub issues page
- `--version` command with author info
- Comprehensive README.md with examples
- MIT License
- Installation script (install.sh)

### Changed
- Migrated from Python 2 to Python 3
- Replaced interactive menu with command-line arguments
- Removed Rich library dependency
- Simplified UI design
- Improved error handling
- Optimized encryption/decryption logic

### Removed
- Interactive menu system
- Python 2 specific code
- Colorama dependency (replaced with custom color module)
- Team attribution (now solo project)

## [2.0] - Previous Version

### Features
- Interactive menu with Rich library
- Basic encryption methods
- Python 2 compatibility

## [1.0] - Initial Release

### Features
- Basic Python obfuscation
- Marshal and Base64 encoding
- Python 2 only
