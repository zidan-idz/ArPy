# Changelog

All notable changes to ArPy will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.1] - Latest Version (Public)

A maintenance and stability update following the major 3.0 rewrite, focusing on
improving reliability, correctness, and clarity in decryption behavior.

### Fixed
- Fixed `bitwise` decryption logic (now fully reversible).
- Fixed `charlen` decryption logic (now fully reversible).
- Improved clarity in `marshal` decryption feedback (explicitly marked as one-way).

### Added
- Added comprehensive test suite in the `testing/` directory to improve long-term
  stability and regression tracking.

---

## [3.0] - Major Release (Public)

A complete modernization of ArPy, transitioning from the legacy interactive design
to a fully modular, Python-3-native architecture.

### Added
- Fully rewritten architecture with a modular design.
- Simple CLI interface using `argparse`.
- 10 basic Python obfuscation methods (adding 3 new techniques from v2.0).
- Automatic method detection for decryption.
- Progress bars for long operations (using `tqdm`).
- Centralized version management.
- Built-in bug reporting system (`--report`).

### Changed
- Full compatibility with Python 3.
- Replaced the old interactive menu with structured command-line arguments.
- Improved error handling throughout.
- Optimized encryption and decryption logic for speed and clarity.

---

## [2.0] - Legacy Release (Not Public)

A transitional version aimed at moving away from Python 2 and expanding beyond
the very limited feature set of 1.0. Although never publicly released, it served
as the foundation for the full rewrite in 3.0.

### Features
- Interactive menu system.
- 7 basic Python obfuscation methods (adding 4 new techniques from v1.0).
- Partial Python 3 compatibility.

---

## [1.0] - Initial Release (Not Public)

The earliest functional version of ArPy, providing a simple set of obfuscation
tools built for Python 2.

### Features
- 3 basic Python obfuscation methods.
- Marshal and Base64 encoding.
- Python 2 only.

---
