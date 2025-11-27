"""Custom color module for ArPy - No external dependencies"""

class Color:
    # ANSI Color Codes
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # Foreground Colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright Foreground Colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

def colored(text, color):
    """Return colored text"""
    return f"{color}{text}{Color.RESET}"

def success(text):
    """Green success message"""
    return colored(f"[+] {text}", Color.GREEN)

def error(text):
    """Red error message"""
    return colored(f"[-] {text}", Color.RED)

def info(text):
    """Cyan info message"""
    return colored(f"[i] {text}", Color.CYAN)

def warning(text):
    """Yellow warning message"""
    return colored(f"[!] {text}", Color.YELLOW)
