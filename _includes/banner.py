from colorama import Fore
import os
import shutil

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    terminal_width, _ = shutil.get_terminal_size()
    banner_lines = [
        Fore.CYAN + "░██████╗░██████╗░░█████╗░░██████╗░██████╗  ██████╗░██████╗░██████╗░░█████╗░██████╗░",
        Fore.CYAN + "██╔════╝░██╔══██╗██╔══██╗██╔════╝██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗",
        Fore.CYAN + "██║░░██╗░██████╔╝███████║╚█████╗░╚█████╗░  ██████╔╝██║░░██║██████╔╝██║░░██║██████╔╝",
        Fore.CYAN + "██║░░╚██╗██╔══██╗██╔══██║░╚═══██╗░╚═══██╗  ██╔══██╗██║░░██║██╔══██╗██║░░██║██╔═══╝░",
        Fore.CYAN + "╚██████╔╝██║░░██║██║░░██║██████╔╝██████╔╝  ██║░░██║██████╔╝██║░░██║╚█████╔╝██║░░░░░",
        Fore.CYAN + "░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═════╝░  ╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░",
        Fore.LIGHTBLACK_EX + "v0.2 - by_dualkeyboards",
    ]
    for line in banner_lines:
        padding = (terminal_width - len(line) + 6) // 2
        print(" " * padding + line)