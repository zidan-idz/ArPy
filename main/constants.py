from .color import Color, colored
from . import __version__, __github__

BANNER_LOADING = """
           =--           
        ----=====        
     --  =======  ==     
  -----=   ===   ===++++ 
   --====  ===  ===+++   
  -==============++++++  
         ======+         
  ==========+++++++++++  
   ======  +++  +++++*   
  =====+   +++   ++++*** 
     =+  +++++++  +*     
        +++++++++        
           +++                              
"""

BANNER = f"""
{Color.CYAN}
                                               
▄████▄ ▄▄▄▄  █████▄ ▄▄ ▄▄ 
██▄▄██ ██▄█▄ ██▄▄█▀ ▀███▀ 
██  ██ ██ ██ ██       █                         
{Color.RESET}
{Color.YELLOW}    VERSION {__version__}{Color.RESET}

{Color.BRIGHT_BLACK}{__github__}{Color.RESET}
"""

CONTACT_INFO = f"""
{Color.YELLOW}Report Bugs / Contact:{Color.RESET}
  {Color.GREEN}WhatsApp:{Color.RESET} 083892081021
  {Color.GREEN}Github:{Color.RESET}   github.com/zidanidz
"""

ABOUT_INFO = f"""
{Color.CYAN}ArPy v{__version__}{Color.RESET}
A Python obfuscation tool for protection and education.
Refactored with modular architecture.
"""
