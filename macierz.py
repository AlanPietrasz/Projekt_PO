from typing import Any
import numpy as np
import pandas as pd
from colorama import Fore, Style

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


# m1 = Macierz(15, 5)
# m1[2, 3] = 10
# m1.print(2, 5)

# mv = m1.get_value()
# print(mv)