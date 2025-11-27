# ArPy Documentation

## Screenshots

### 1. Menu Method
![Menu Method](img1.png)

The menu list shows all available method and short description.

### 2. Usage Example
![Usage Example](img2.png)

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
- `img1.png` - ArPy banner and help menu
- `img2.png` - Encryption example with progress bar
- `help_output.txt` - Full help text
- `list_output.txt` - List of all methods
