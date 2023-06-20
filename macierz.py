from typing import Any
import numpy as np
import pandas as pd
from colorama import Fore, Style

from aux import *
from obiekt_matematyczny import ObiektMatematyczny 


class Macierz(ObiektMatematyczny):
    MAX_MATRIX_SIZE = 20
    nazwa_typu = "MACIERZ"
    
    def __init__(self, m, n, nazwa = "", tab=[]):
        self.m = m
        self.n = n

        if tab == []:
            tab = np.zeros((m, n), dtype=object)
        self.macierz = np.reshape(tab, (m, n))
        if nazwa == "":
            self.has_a_name = False
            self.nazwa = repr(self.macierz)
        else:
            self.has_a_name = True
            self.nazwa = nazwa
            
    def copy(self, dtype=object):
        nowy_obiekt = Macierz(self.m, self.n)
        for i in range(1, self.m+1):
            for j in range(1, self.n+1):
                nowy_obiekt[i, j] = self[i, j]
        return nowy_obiekt
        
    def get_value(self):
        return self.macierz    
    
    def get_dimensions(self):
        return (self.m, self.n)

    def is_symmetric(self):
        mac_float = self.macierz.astype(float)
        return np.allclose(mac_float, mac_float.T)

    def eq_dimensions(self, m = 0, n = 0):
        if m != 0:
            if self.m != m:
                return False
        if n != 0:
            if self.n != n:
                return False
        return True
    
    def swap_rows(self, row1, row2):
        self.macierz[[row1-1, row2-1]] = self.macierz[[row2-1, row1-1]]
        #self.macierz = np.swaprows(self.macierz, row1-1, row2-1)

    def __getitem__(self, indices):
        i, j = indices
        return self.macierz[i-1, j-1]

    def __setitem__(self, indices, value):
        i, j = indices
        self.macierz[i-1, j-1] = value
        
    def __repr__(self):
        return self.nazwa
    
    def __str__(self):
        return self.to_str()
    
    def eval(self):
        for i in range(self.m):
            for j in range(self.n):
                self.macierz[i, j] = eval(self.macierz[i, j])
                
    def modify(self, is_wektor = False):
        self.edit_matrix(self.m, self.n, is_wektor)
        
    def to_str(self, color_list=[], color=Fore.GREEN, color2=Fore.CYAN):
        res = ""
        arr = self.macierz
        max_width = np.vectorize(lambda x: len(str(x)))(arr).max()
        n_len = len(str(self.n))
        m_len = len(str(self.m))
        res += " " * (2 + n_len)
        for j in range(arr.shape[1]):
            res += " " * (max_width - len(str(j)))
            res += f"{color2}{j+1}:{Style.RESET_ALL}"
        res += "\n"
        for i in range(arr.shape[0]):
            res += f"{color2}{i+1}:{Style.RESET_ALL} "
            res += " " * (m_len - (len(str(i+1))))
            for j in range(arr.shape[1]):
                if (i + 1, j + 1) in color_list:
                    res += f"{color}{str(arr[i, j]).rjust(max_width)}{Style.RESET_ALL} "
                else:
                    res += str(arr[i, j]).rjust(max_width) + " "
            res += "\n"
        return res
    
    def to_str_2_col(self, color_list=[], color3_list = [], color=Fore.GREEN, color2=Fore.CYAN, color3=Fore.MAGENTA):
        res = ""
        arr = self.macierz
        max_width = np.vectorize(lambda x: len(str(x)))(arr).max()
        n_len = len(str(self.n))
        m_len = len(str(self.m))
        res += " " * (2 + n_len)
        for j in range(arr.shape[1]):
            res += " " * (max_width - len(str(j)))
            res += f"{color2}{j+1}:{Style.RESET_ALL}"
        res += "\n"
        for i in range(arr.shape[0]):
            res += f"{color2}{i+1}:{Style.RESET_ALL} "
            res += " " * (m_len - (len(str(i+1))))
            for j in range(arr.shape[1]):
                if (i + 1, j + 1) in color_list:
                    res += f"{color}{str(arr[i, j]).rjust(max_width)}{Style.RESET_ALL} "
                elif (i + 1, j + 1) in color3_list:
                    res += f"{color3}{str(arr[i, j]).rjust(max_width)}{Style.RESET_ALL} "
                else:
                    res += str(arr[i, j]).rjust(max_width) + " "
            res += "\n"
        return res
        
    def print(self, color_list = [], color=Fore.GREEN, color2=Fore.CYAN):
        print(self.to_str(color_list, color, color2))

    def print_np(self):
        print(self.macierz)

    def enter_matrix_size(message):
        while True:
            print(message)
            user_input = input()
            if user_input.isdigit():
                s = int(user_input)
                if s < 1 or s > Macierz.MAX_MATRIX_SIZE:
                    print("Podano nieprawidłową wartość")
                    user_input = input()
                    clear_terminal()
                else:
                    return s
            else:
                print("Podano nieprawidłową wartość")
                user_input = input()
                clear_terminal()
    
    def create_matrix(nazwa="", m=0, n=0, equal=False):
        clear_terminal()
        if m == 0:
            m = Macierz.enter_matrix_size("Podaj liczbę wierszy")
        if n == 0:
            n = m
            if not equal:
                n = Macierz.enter_matrix_size("Podaj liczbę kolumn")
        macierz = Macierz(m, n, nazwa)
        return Macierz.edit_matrix(macierz, m, n, is_wektor = False)
    
    def edit_matrix(macierz, m, n, is_wektor = False):
        i = 1
        j = 1
        while True:
            clear_terminal()
            macierz.print([(i, j)])
            print(f"Używaj wasd, aby poruszać się po {'wektorze' if is_wektor else 'macierzy'}")
            print("Naciśnij ENTER jeśli chcesz wpisać wartość w wybrane pole")
            print(f"Naciśnij q jeśli chcesz zakończyć wypełnianie pól {'wektora' if is_wektor else 'macierzy'}")
            user_input = get_char()
            if user_input == "enter":
                wartosc = ObiektMatematyczny.create_number_val()
                macierz[i, j] = wartosc
            elif user_input == "w":
                if i > 1:
                    i -= 1
            elif user_input == "a":
                if j > 1:
                    j -= 1
            elif user_input == "s":
                if i < m:
                    i += 1
            elif user_input == "d":
                if j < n:
                    j += 1
            elif user_input == "q":
                break
            # else:
            #     invalid_input("Podano nieprawidłową wartość")
        return macierz

    def enter_matrix():
        while(True):
            print("------------MENU-GŁÓWNE-----------------")
            print("1. Utwórz nową macierz")
            print("2. Wybierz macierz zapisaną w pamięci")
            print("Podaj liczbę:   ", end="")
            user_input = input()
            if user_input == "1":
                nowy_obiekt = Macierz.create_matrix()
            elif user_input == "2":
                pass
            else:
                invalid_input("Podano niepoprawne dane")
                

    # def print(self, row=-1, col=-1, color=Fore.GREEN, color2=Fore.CYAN):
    #     arr = self.macierz
    #     max_width = np.vectorize(lambda x: len(str(x)))(arr).max()
    #     n_len = len(str(self.n))
    #     m_len = len(str(self.m))
    #     print(" " * (3 + n_len), end="")
    #     for j in range(arr.shape[1]):
    #         print(f"{color2}{j+1}:{Style.RESET_ALL}", end=" " * (max_width - len(str(j))))
    #     print()

    #     for i in range(arr.shape[0]):
    #         print(f"{color2}{i+1}:{Style.RESET_ALL}", end=" ")
    #         print(" " * (m_len - (len(str(i+1)))), end="")
    #         for j in range(arr.shape[1]):
    #             if i == row - 1 and j == col - 1:
    #                 print(f"{color}{str(arr[i, j]).ljust(max_width)}{Style.RESET_ALL}", end=" ")
    #             else:
    #                 print(str(arr[i, j]).ljust(max_width), end=" ")
    #         print()


    # def print(self, row=-1, col=-1, color=Fore.GREEN, color2=Fore.CYAN):
    #     arr = self.macierz
    #     max_width = np.vectorize(lambda x: len(str(x)))(arr).max()
    #     n_len = len(str(self.n))
    #     m_len = len(str(self.m))
    #     print(" " * (2 + n_len), end="")
    #     for j in range(arr.shape[1]):
    #         print(" " * (max_width - len(str(j))), end="")
    #         print(f"{color2}{j+1}:{Style.RESET_ALL}", end="")
    #     print()

    #     for i in range(arr.shape[0]):
    #         print(f"{color2}{i+1}:{Style.RESET_ALL}", end=" ")
    #         print(" " * (m_len - (len(str(i+1)))), end="")
    #         for j in range(arr.shape[1]):
    #             if i == row - 1 and j == col - 1:
    #                 print(f"{color}{str(arr[i, j]).rjust(max_width)}{Style.RESET_ALL}", end=" ")
    #             else:
    #                 print(str(arr[i, j]).rjust(max_width), end=" ")
    #         print()

# m1 = Macierz(15, 5)
# m1[2, 3] = 10
# m1.print(2, 5)

# mv = m1.get_value()
# print(mv)