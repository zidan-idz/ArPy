import time
from colorama import Fore, Style
from tqdm import tqdm
from .constants import CONTACT_INFO, ABOUT_INFO

class Features:
    def update_tool(self):
        print(f"\n{Fore.CYAN}Checking for updates...{Style.RESET_ALL}")
        try:
            import subprocess
            # Check if git is installed
            subprocess.check_call(["git", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            # Pull changes
            print(f"{Fore.YELLOW}Pulling latest changes from repository...{Style.RESET_ALL}")
            process = subprocess.run(["git", "pull"], capture_output=True, text=True)
            
            if process.returncode == 0:
                print(f"\n{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} Tool updated successfully!")
                print(process.stdout)
                print(f"{Fore.CYAN}Please restart the tool to apply changes.{Style.RESET_ALL}")
            else:
                print(f"\n{Fore.RED}[ERROR]{Style.RESET_ALL} Update failed.")
                print(process.stderr)
        except FileNotFoundError:
             print(f"\n{Fore.RED}[ERROR]{Style.RESET_ALL} Git is not installed. Please install git or update manually.")
        except Exception as e:
            print(f"\n{Fore.RED}[ERROR]{Style.RESET_ALL} An error occurred: {e}")

    def show_report(self):
        print(CONTACT_INFO)
        input(f"\n{Fore.WHITE}Press Enter to return...{Style.RESET_ALL}")

    def show_about(self):
        print(ABOUT_INFO)
        input(f"\n{Fore.WHITE}Press Enter to return...{Style.RESET_ALL}")
