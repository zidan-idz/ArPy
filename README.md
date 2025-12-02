<div align="center">

![ArPy Banner](docs/banner.webp)

<div align="center">

[![Author](https://img.shields.io/badge/Author-Zidan%20IDz-%2300BFFF?style=for-the-badge&logo=github)](https://github.com/zidan-idz)
[![Version](https://img.shields.io/badge/Version-3.1%20-%2300BFFF?style=for-the-badge)](https://github.com/zidan-idz/Theme-Me/releases)
[![Language](https://img.shields.io/badge/Language-Python-%2300BFFF?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-%2300BFFF?style=for-the-badge)](LICENSE)

</div>



</div>

## Screenshots

### Menu & Commands
![ArPy Method](docs/img1.webp)

### Usage Example
![ArPy Usage](docs/img2.webp)


## Features

- 🔒 **10 Encryption Methods** - Multiple obfuscation techniques.
- 🔓 **Auto-Decryption** - Intelligent method detection.
- ⚡ **Fast & Efficient** - Optimized with progress bars.
- 🎨 **Clean CLI** - Simple command-line interface.
- 📦 **Open Source** - Fully transparent, community-driven, and easy to extend.


## Installation

```bash
git clone https://github.com/zidan-idz/ArPy.git
cd ArPy
pip install -r requirements.txt
```

Or use the install script:
```bash
bash install.sh
```

## Usage

### Basic Encryption
```bash
python run.py -e base64 script.py
```

### Encryption with Iterations
```bash
python run.py -e marshal -i 5 script.py
```

### Custom Output Path
```bash
python run.py -e zlib script.py -o encrypted_output.py
```

### Decryption
```bash
python run.py -d base64 encrypted.py
```

### Auto-Detect Decryption
```bash
python run.py -d auto encrypted.py
```

### List Available Methods
```bash
python run.py --list
```

## Encryption Methods

| Method | Description | Iterations |
|--------|-------------|------------|
| `marshal` | Compile to bytecode | ✓ |
| `zlib` | Compress using zlib | ✓ |
| `base64` | Encode using Base64 | ✓ |
| `base32` | Encode using Base32 | ✓ |
| `base16` | Encode using Base16 | ✓ |
| `lambda` | Lambda + XOR obfuscation | ✗ |
| `bitwise` | Boolean/Bitwise arithmetic | ✗ |
| `binhex` | Massive integer encoding | ✗ |
| `charlen` | Character length encoding | ✗ |
| `revzlib` | Reverse + Zlib + Base64 | ✗ |

## Decryption Methods

All encryption methods are supported for decryption, plus:
- `auto` - Automatically detect and decrypt

## Command-Line Options

```
usage: run.py [-h] [-e METHOD] [-d METHOD] [-i N] [-o FILE] [--list] [--version] [file]

ArPy - Python Obfuscation Tool v3.1

positional arguments:
  file                  Input file to process

options:
  -h, --help            show this help message and exit
  -e METHOD, --encrypt METHOD
                        Encryption method
  -d METHOD, --decrypt METHOD
                        Decryption method
  -i N, --iterations N  Number of iterations (max 50, default: 1)
  -o FILE, --output FILE
                        Output file path
  --list                List all available methods
  --version             show program's version number and exit
```

## Dependencies

- Python 3.7+
- tqdm 4.66+ (for progress bars)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Zidan IDz**

- GitHub: [@zidan-idz](https://github.com/zidan-idz)
- Facebook: [@Zidan_IDz](https://facebook.com/muhammadraid.zaidani)
- Instagram: [@zidan_idz](https://instagram.com/zidan_idz)

## Disclaimer

This tool is for educational purposes and legitimate code protection only. Do not use it for malicious purposes. The author is not responsible for any misuse of this software.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

### v3.1 (Latest Version)
A maintenance and stability update focusing on reliability and correctness.
- Fixed `bitwise` and `charlen` decryption logic (now fully reversible).
- Added comprehensive test suite for stability.
- Improved clarity in `marshal` decryption feedback.

---
