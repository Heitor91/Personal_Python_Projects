import os

from colorama import Fore, Back, Style, init
init(autoreset=True)

print(Fore.RED + 'Red Text')
print(Back.YELLOW + 'back')
print(Back.LIGHTYELLOW_EX + 'back')
print(Style.BRIGHT + 'Dim is')
print(Style.RESET_ALL)
print('Normal')
