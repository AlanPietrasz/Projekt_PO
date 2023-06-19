import os
import numpy as np

import platform
import sys
import tty
import termios

def get_length(element):
    return len(element) if isinstance(element, str) else len(str(element))


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_char():
    if platform.system() == 'Windows':
        import msvcrt
        return msvcrt.getch().decode()
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            # val = sys.stdin.read(1)
            # return val
            char = sys.stdin.read(1)
            if ord(char) == 13:  # Kod ASCII dla klawisza Enter
                # Jeśli wcisnięto Enter, zwróć pusty znak
                return "enter"
            return char
            
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            
def invalid_input(message):
    print()
    print(message)
    user_input = input()
    clear_terminal()

