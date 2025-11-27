# ArPy - Python Obfuscation Tool

<div align="center">

```
▄████▄ ▄▄▄▄  █████▄ ▄▄ ▄▄ 
██▄▄██ ██▄█▄ ██▄▄█▀ ▀███▀ 
██  ██ ██ ██ ██       █   
```

**A simple Python obfuscation tool for code protection**

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-3.0-orange.svg)](https://github.com/zidan-idz/ArPy)

</div>

## Screenshots

### Banner & Help
![ArPy Banner](docs/banner.png)

### Usage Example
![ArPy Usage](docs/usage_example.png)


## Features

- 🔒 **10 Encryption Methods** - Multiple obfuscation techniques
- 🔓 **Auto-Decryption** - Intelligent method detection
- ⚡ **Fast & Efficient** - Optimized with progress bars
- 🎨 **Clean CLI** - simple command-line interface
- 📦 **Lightweight** - Minimal dependencies

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

## Examples

### Example 1: Simple Obfuscation
```bash
# Encrypt a script
python run.py -e base64 my_script.py

# Output: my_script_enc.py
```

### Example 2: Multi-Layer Encryption
```bash
# Apply 10 iterations of marshal encoding
python run.py -e marshal -i 10 sensitive_code.py
```

### Example 3: Decrypt Unknown Method
```bash
# Auto-detect and decrypt
python run.py -d auto obfuscated_file.py
```

## Command-Line Options

```
usage: run.py [-h] [-e METHOD] [-d METHOD] [-i N] [-o FILE] [--list] [--version] [file]

ArPy - Python Obfuscation Tool v3.0

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

## Project Structure

```
ArPy/
├── run.py              # Main CLI entry point
├── main/
│   ├── __init__.py     # Package info
│   ├── color.py        # Custom color module
│   ├── constants.py    # Banner and constants
│   ├── encrypt.py      # Encryption logic
│   ├── decrypt.py      # Decryption logic
│   └── utils.py        # Utility functions
├── docs/
│   ├── README.md       # Documentation
│   ├── banner.png      # Screenshot: Banner & Help
│   ├── usage_example.png # Screenshot: Usage Example
│   ├── help_output.txt # Full help text
│   └── list_output.txt # Methods list
├── requirements.txt    # Dependencies
├── install.sh          # Installation script
├── CHANGELOG.md        # Version history
├── LICENSE             # MIT License
└── README.md           # This file
```

## Dependencies

- Python 3.7+
- tqdm (for progress bars)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Zidan IDz**

- GitHub: [@zidan-idz](https://github.com/zidan-idz)
- WhatsApp: 083892081021

## Disclaimer

This tool is for educational purposes and legitimate code protection only. Do not use it for malicious purposes. The author is not responsible for any misuse of this software.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

### v3.0 (2025-11-27)
- Complete rewrite with modular architecture
- Simple CLI interface with argparse
- Custom color module (no external color dependencies)
- 10 encryption methods
- Auto-detection decryption
- Progress bars for long operations
- Comprehensive documentation
- Centralized version management
- Bug reporting system (--report)

---

<div align="center">
Made with ❤️ by Zidan IDz
</div>
