# ArPy Documentation

## Screenshots

### 1. Menu Method
![ArPy Method](img1.webp)

The menu list shows all available methods and short descriptions.

### 2. Usage Example
![Usage Example](img2.webp)

Example of encrypting a file with progress bar.

## Command Examples

### Basic Encryption
```bash
python run.py -e base64 script.py
```

### Multi-iteration Encryption
```bash
python run.py -e marshal -i 10 script.py
```

### Decryption
```bash
python run.py -d auto encrypted.py
```

### List Methods
```bash
python run.py --list
```

## Output Files

All output files are saved in the `docs/` directory:
- `img1.webp` - ArPy menu method
- `img2.webp` - Encryption example
- `help_output.txt` - Full help text
- `list_output.txt` - List of all methods
