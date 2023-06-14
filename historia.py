
from collections import defaultdict as dd
from colorama import Fore, Style

from aux import clear_terminal

class Historia:
    def __init__(self):
        self.slownik_indeks_klucz = list()
        self.slownik_nazwa_wartosc = dd()
        self.update_len()
        
    def __setitem__(self, nazwa, wartosc):
        self.slownik_indeks_klucz.append(nazwa)
        self.update_len()
        self.slownik_nazwa_wartosc[nazwa] = wartosc
        
    def __getitem__(self, ind):
        return Historia.get_val(self.slownik_indeks_klucz[ind-1])
        
    def get_val(self, nazwa):
        return self.slownik_nazwa_wartosc[nazwa]
    
    def print_range(self, b, e):
        clear_terminal()
        print("---------HISTORIA-----------")
        max_len = len(str(e))
        for i in range(b-1, e):
            print(f"{Fore.GREEN}{i+1}: {Style.RESET_ALL}", end="")
            print(" " * (max_len - (len(str(i+1)))), end="")
            print(repr(self.slownik_nazwa_wartosc[self.slownik_indeks_klucz[i]]))
    
    def update_len(self):
        self.dlugosc_historii = len(self.slownik_indeks_klucz)        
            
    def print_all(self):
        Historia.print_range(self, 1, self.dlugosc_historii)