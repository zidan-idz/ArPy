from colorama import Fore, Style
from .constants import BANNER

class UI:
    def show_banner(self):
        from .utils import clear_screen
        clear_screen()
        print(BANNER)

    def show_main_menu(self):
        self.show_banner()
        print(f"{Fore.CYAN}MAIN MENU{Style.RESET_ALL}\n")
        options = [
            ("01", "Encrypt File"),
            ("02", "Decrypt File"),
            ("03", "Update Tool"),
            ("04", "Report Bug"),
            ("05", "About"),
            ("00", "Exit")
        ]
        for num, name in options:
            print(f"  {Fore.YELLOW}{num}.{Style.RESET_ALL} {name}")
        
        choice = input(f"\n{Fore.GREEN}Select:{Style.RESET_ALL} ").strip()
        return choice

    def show_encrypt_menu(self):
        self.show_banner()
        print(f"{Fore.CYAN}ENCRYPTION METHODS{Style.RESET_ALL}\n")
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
            print(f"  {Fore.YELLOW}{num}.{Style.RESET_ALL} {name}")
        
        choice = input(f"\n{Fore.GREEN}Select:{Style.RESET_ALL} ").strip()
        return choice

    def show_decrypt_menu(self):
        self.show_banner()
        print(f"{Fore.CYAN}DECRYPTION METHODS{Style.RESET_ALL}\n")
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
            print(f"  {Fore.YELLOW}{num}.{Style.RESET_ALL} {name}")
        
        choice = input(f"\n{Fore.GREEN}Select:{Style.RESET_ALL} ").strip()
        return choice

    def get_file_path(self):
        return input(f"\n{Fore.CYAN}File path:{Style.RESET_ALL} ").strip()

    def get_iterations(self):
        try:
            iterations = int(input(f"{Fore.CYAN}Iterations (max 50) [1]:{Style.RESET_ALL} ").strip() or "1")
            return min(iterations, 50)
        except ValueError:
            return 1

    def show_success(self, path):
        print(f"\n{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} Saved to: {Fore.YELLOW}{path}{Style.RESET_ALL}")
        input(f"\n{Fore.WHITE}Press Enter to continue...{Style.RESET_ALL}")

    def show_error(self, msg):
        print(f"\n{Fore.RED}[ERROR]{Style.RESET_ALL} {msg}")
        input(f"\n{Fore.WHITE}Press Enter to continue...{Style.RESET_ALL}")

    def show_message(self, msg):
        print(f"\n{msg}")
        input(f"\n{Fore.WHITE}Press Enter to continue...{Style.RESET_ALL}")
