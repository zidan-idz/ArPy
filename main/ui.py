from .color import Color
from .constants import BANNER

class UI:
    def show_banner(self):
        from .utils import clear_screen
        clear_screen()
        print(BANNER)

    def show_main_menu(self):
        self.show_banner()
        print(f"{Color.CYAN}MAIN MENU{Color.RESET}\n")
        options = [
            ("01", "Encrypt File"),
            ("02", "Decrypt File"),
            ("03", "Update Tool"),
            ("04", "Report Bug"),
            ("05", "About"),
            ("00", "Exit")
        ]
        for num, name in options:
            print(f"  {Color.YELLOW}{num}.{Color.RESET} {name}")
        
        choice = input(f"\n{Color.GREEN}Select:{Color.RESET} ").strip()
        return choice

    def show_encrypt_menu(self):
        self.show_banner()
        print(f"{Color.CYAN}ENCRYPTION METHODS{Color.RESET}\n")
        options = [
            ("01", "Marshal (Bytecode)"),
            ("02", "Zlib (Compress)"),
            ("03", "Base64"),
            ("04", "Base32"),
            ("05", "Base16"),
            ("06", "Marshal + Base64"),
            ("07", "Lambda (XOR)"),
            ("08", "Bitwise (Boolean)"),
            ("09", "BinHex (Integer)"),
            ("10", "CharLen (Hard)"),
            ("11", "RevZlib (Reverse)"),
            ("00", "Back")
        ]
        for num, name in options:
            print(f"  {Color.YELLOW}{num}.{Color.RESET} {name}")
        
        choice = input(f"\n{Color.GREEN}Select:{Color.RESET} ").strip()
        return choice

    def show_decrypt_menu(self):
        self.show_banner()
        print(f"{Color.CYAN}DECRYPTION METHODS{Color.RESET}\n")
        options = [
            ("01", "Marshal (Bytecode)"),
            ("02", "Zlib (Compress)"),
            ("03", "Base64"),
            ("04", "Base32"),
            ("05", "Base16"),
            ("06", "Auto-Detect"),
            ("07", "Lambda (XOR)"),
            ("08", "Bitwise (Boolean)"),
            ("09", "BinHex (Integer)"),
            ("10", "CharLen (Hard)"),
            ("11", "RevZlib (Reverse)"),
            ("00", "Back")
        ]
        for num, name in options:
            print(f"  {Color.YELLOW}{num}.{Color.RESET} {name}")
        
        choice = input(f"\n{Color.GREEN}Select:{Color.RESET} ").strip()
        return choice

    def get_file_path(self):
        return input(f"\n{Color.CYAN}File path:{Color.RESET} ").strip()

    def get_iterations(self):
        try:
            iterations = int(input(f"{Color.CYAN}Iterations (max 50) [1]:{Color.RESET} ").strip() or "1")
            return min(iterations, 50)
        except ValueError:
            return 1

    def show_success(self, path):
        print(f"\n{Color.GREEN}[SUCCESS]{Color.RESET} Saved to: {Color.YELLOW}{path}{Color.RESET}")
        input(f"\n{Color.WHITE}Press Enter to continue...{Color.RESET}")

    def show_error(self, msg):
        print(f"\n{Color.RED}[ERROR]{Color.RESET} {msg}")
        input(f"\n{Color.WHITE}Press Enter to continue...{Color.RESET}")

    def show_message(self, msg):
        print(f"\n{msg}")
        input(f"\n{Color.WHITE}Press Enter to continue...{Color.RESET}")
