import pyfiglet

import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=False)

figlet = pyfiglet.Figlet(font="doom")
print(colorama.Fore.GREEN + 
      figlet.renderText("pyproj")
      + colorama.Fore.RESET)
    
colorama.init(autoreset=True)

print("PyProj - a python project creator")
print("                    (c) konradsic")