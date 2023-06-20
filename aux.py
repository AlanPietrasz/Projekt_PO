import os
import math

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
            char = sys.stdin.read(1)
            if ord(char) == 13:
                return "enter"
            return char
            
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            
def invalid_input(message):
    print()
    print(message)
    user_input = input()
    clear_terminal()


import math

def round_to_n_significant_digits(number, n):
    if number == 0:
        return 0

    power = math.floor(math.log10(abs(number))) + 1
    scale = 10 ** (n - power)
    rounded_number = round(number * scale) / scale
    return rounded_number