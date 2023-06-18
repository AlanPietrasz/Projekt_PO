from typing import Any
import numpy as np
import pandas as pd
from colorama import Fore, Style

from aux import *
from obiekt_matematyczny import ObiektMatematyczny 


class Macierz(ObiektMatematyczny):
    MAX_MATRIX_SIZE = 20
    
    def __init__(self, m, n, nazwa = "", tab=[]):
        self.m = m
        self.n = n

        if tab == []:
            tab = np.zeros((m, n))
        self.macierz = np.reshape(tab, (m, n))
        if nazwa == "":
            self.has_a_name = False
            self.set_name(repr(self.macierz))
        else:
            self.has_a_name = True
            self.set_name(nazwa)
        
    def get_value(self):
        return self.macierz    
    
    def get_dimensions(self):
        return (self.m, self.n)

    def __getitem__(self, indices):
        i, j = indices
        return self.macierz[i-1, j-1]

    def __setitem__(self, indices, value):
        i, j = indices
        self.macierz[i-1, j-1] = value
        if not self.has_a_name:
            self.set_name(repr(self.macierz))
        
    def __repr__(self):
        return self.nazwa
    
    def __str__(self):
        return str(self.macierz)
    
    def eval(self):
        for i in range(self.m):
            for j in range(self.n):
                self.macierz[i, j] = eval(self.macierz[i, j])
        
        
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


    def print(self, row=-1, col=-1, color=Fore.GREEN, color2=Fore.CYAN):
        arr = self.macierz
        max_width = np.vectorize(lambda x: len(str(x)))(arr).max()
        n_len = len(str(self.n))
        m_len = len(str(self.m))
        print(" " * (2 + n_len), end="")
        for j in range(arr.shape[1]):
            print(" " * (max_width - len(str(j))), end="")
            print(f"{color2}{j+1}:{Style.RESET_ALL}", end="")
        print()

        for i in range(arr.shape[0]):
            print(f"{color2}{i+1}:{Style.RESET_ALL}", end=" ")
            print(" " * (m_len - (len(str(i+1)))), end="")
            for j in range(arr.shape[1]):
                if i == row - 1 and j == col - 1:
                    print(f"{color}{str(arr[i, j]).rjust(max_width)}{Style.RESET_ALL}", end=" ")
                else:
                    print(str(arr[i, j]).rjust(max_width), end=" ")
            print()


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
    
    def create_matrix(nazwa):
        clear_terminal()
        m = Macierz.enter_matrix_size("Podaj liczbę wierszy")
        n = Macierz.enter_matrix_size("Podaj liczbę kolumn")
        macierz = Macierz(m, n, nazwa)
        return Macierz.edit_matrix(macierz, m, n, is_wektor = False)
    
    def edit_matrix(macierz, m, n, is_wektor = False):
        i = 1
        j = 1
        while True:
            clear_terminal()
            macierz.print(i, j)
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
            else:
                print("Podano nieprawidłową wartość")
                user_input = input()
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
                


# m1 = Macierz(15, 5)
# m1[2, 3] = 10
# m1.print(2, 5)

# mv = m1.get_value()
# print(mv)