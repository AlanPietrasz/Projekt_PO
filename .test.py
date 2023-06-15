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
