import os

import platform
import sys
import tty
import termios


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
            


