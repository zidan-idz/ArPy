import time
from colorama import Fore, Style
from tqdm import tqdm
from .constants import CONTACT_INFO, ABOUT_INFO

class Features:
    def update_tool(self):
        print(f"\n{Fore.CYAN}Checking for updates...{Style.RESET_ALL}")
        for _ in tqdm(range(100), desc="Updating", bar_format='{l_bar}{bar}'):
            time.sleep(0.02)
        print(f"\n{Fore.GREEN}[INFO]{Style.RESET_ALL} You are using the latest version (v3.0)!")
        input(f"\n{Fore.WHITE}Press Enter to return...{Style.RESET_ALL}")

    def show_report(self):
        print(CONTACT_INFO)
        input(f"\n{Fore.WHITE}Press Enter to return...{Style.RESET_ALL}")

    def show_about(self):
        print(ABOUT_INFO)
        input(f"\n{Fore.WHITE}Press Enter to return...{Style.RESET_ALL}")
