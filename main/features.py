import time
from .color import Color
from tqdm import tqdm
from .constants import CONTACT_INFO, ABOUT_INFO

class Features:
    def update_tool(self):
        print(f"\n{Color.CYAN}Checking for updates...{Color.RESET}")
        try:
            import subprocess
            # Check if git is installed
            subprocess.check_call(["git", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            # Pull changes
            print(f"{Color.YELLOW}Pulling latest changes from repository...{Color.RESET}")
            process = subprocess.run(["git", "pull"], capture_output=True, text=True)
            
            if process.returncode == 0:
                print(f"\n{Color.GREEN}[SUCCESS]{Color.RESET} Tool updated successfully!")
                print(process.stdout)
                print(f"{Color.CYAN}Please restart the tool to apply changes.{Color.RESET}")
            else:
                print(f"\n{Color.RED}[ERROR]{Color.RESET} Update failed.")
                print(process.stderr)
        except FileNotFoundError:
             print(f"\n{Color.RED}[ERROR]{Color.RESET} Git is not installed. Please install git or update manually.")
        except Exception as e:
            print(f"\n{Color.RED}[ERROR]{Color.RESET} An error occurred: {e}")

    def show_report(self):
        print(CONTACT_INFO)
        input(f"\n{Color.WHITE}Press Enter to return...{Color.RESET}")

    def show_about(self):
        print(ABOUT_INFO)
        input(f"\n{Color.WHITE}Press Enter to return...{Color.RESET}")
