import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    except Exception as e:
        return None

def save_file(original_path, content, suffix="_enc"):
    base, ext = os.path.splitext(original_path)
    out_path = f"{base}{suffix}{ext}"
    try:
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return out_path
    except Exception as e:
        return None
