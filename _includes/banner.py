# _includes/banner.py
from colorama import Fore
import os

def display_banner():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
    print()
    print()
    print(Fore.CYAN + "          ░██████╗░██████╗░░█████╗░░██████╗░██████╗  ██████╗░██████╗░██████╗░░█████╗░██████╗░")
    print(Fore.CYAN + "          ██╔════╝░██╔══██╗██╔══██╗██╔════╝██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗")
    print(Fore.CYAN + "          ██║░░██╗░██████╔╝███████║╚█████╗░╚█████╗░  ██████╔╝██║░░██║██████╔╝██║░░██║██████╔╝")
    print(Fore.CYAN + "          ██║░░╚██╗██╔══██╗██╔══██║░╚═══██╗░╚═══██╗  ██╔══██╗██║░░██║██╔══██╗██║░░██║██╔═══╝░")
    print(Fore.CYAN + "          ╚██████╔╝██║░░██║██║░░██║██████╔╝██████╔╝  ██║░░██║██████╔╝██║░░██║╚█████╔╝██║░░░░░")
    print(Fore.CYAN + "          ░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═════╝░  ╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░" + Fore.LIGHTBLACK_EX + " 0.2")
    print(Fore.LIGHTBLACK_EX + "                                                                             by_dualkeyboards")
    print()