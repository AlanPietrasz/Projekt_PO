# from aux import clear_terminal
# from pynput import keyboard

# from pynput.keyboard import Key

# def on_key_release(key):
#     if key == Key.right:
#         print("Right key clicked")
#     elif key == Key.left:
#         print("Left key clicked")
#     elif key == Key.up:
#         print("Up key clicked")
#     elif key == Key.down:
#         print("Down key clicked")
#     elif key == Key.esc:
#         exit()
#     elif key == Key.enter:
#         exit()


# with keyboard.Listener(on_release=on_key_release) as listener:
#     listener.join()




# except:
#     break

# from pynput import keyboard
    
# def on_press(key):
#         clear_terminal()
#         if key == keyboard.Key.up:
#             clear_terminal()
#             print('PRESSED')
#         if key == keyboard.Key.esc:
#             listener.stop()
    
    
# with keyboard.Listener(on_press=on_press) as listener:
#         listener.join()

# import keyboard
# import time

# while True:
#     print("Dziala")
#     time.sleep(1)
#     if keyboard.is_pressed('left'):
#         print('You Pressed left!')
#         time.sleep(0.1)
#     if keyboard.is_pressed('right'):
#         print('You Pressed right!')
#         time.sleep(0.1)
#     if keyboard.is_pressed('down'):
#         print('You Pressed down!')
#         time.sleep(0.1)
#     if keyboard.is_pressed('up'):
#         print('You Pressed up!')
#         time.sleep(0.1)
#     if keyboard.is_pressed('esc'):  # Dodany warunek wyjścia po naciśnięciu klawisza Esc
#         break


# import sys

# def get_key():
#     # Odczytaj pojedynczy znak z wejścia
#     if sys.platform == 'win32' or sys.platform == 'cygwin':
#         import msvcrt
#         key = msvcrt.getch()
#     else:
#         # Linux lub macOS
#         import tty, termios
#         fd = sys.stdin.fileno()
#         old_settings = termios.tcgetattr(fd)
#         try:
#             tty.setraw(sys.stdin.fileno())
#             key = sys.stdin.read(1)
#         finally:
#             termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

#     return key

# userinp = input()
# userinp = input()

# while True:
#     pressed_key = get_key()
    

#     print("Naciśnięto klawisz:", pressed_key, )
    
#     # Przerwij pętlę, jeśli naciśnięto klawisz "q"
#     if pressed_key.lower() == 'q':
#         break

for i in range(-2, 2):
    print(i,": ", end="")
    print(str(i).isdigit())
    
for i in range(-2, 2):
    print(i,": ", end="")
    print(str(i).isnumeric())

for i in range(-2, 2):
    print(i,": ", end="")
    print(str(i).isdecimal())
    
for i in range(-2, 2):
    print(i,": ", end="")
    print(str(i).isalnum())
    
print()
print()
print() 
    
for i in range(-2, 2):
    print(i,": ", end="")
    print(str(i+0.5).isdigit())
    
print()
    
# for i in range(-2, 2):
#     print(i,": ", end="")
#     print(str(i+0.5).isnumeric())

for i in range(-2, 2):
    print(i,": ", end="")
    print(str(i+0.5).isdecimal())
    
# for i in range(-2, 2):
#     print(i,": ", end="")
#     print(str(i+0.5).isalnum())
    
#print(int("-10.3"))

        
print(set(range(1, 10)))

print("3a".isdecimal())

print("3a".isdigit())

import numpy as np

# Przykładowe macierze
matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
matrix2 = np.array([[7, 8, 9], [10, 11, 12]])

# Wyświetlanie macierzy obok siebie
print("Matrix 1:\t\tMatrix 2:")
for row1, row2 in zip(matrix1, matrix2):
    print('\t'.join([str(element) for element in row1]) + "\t\t" + '\t'.join([str(element) for element in row2]))


import math

def shift_decimal_point(number):
    abs_number = abs(number)
    power = math.ceil(math.log10(abs_number)) - 1
    shifted_number = number * 10**(-power)
    return shifted_number

# Przykłady użycia
x = 123.45
shifted_x = shift_decimal_point(x)
print(shifted_x)  # Output: 1.2345

y = 0.012345
shifted_y = shift_decimal_point(y)
print(shifted_y)  # Output: 1.2345
