
from collections import defaultdict as dd
from colorama import Fore, Style

from aux import *

class Historia:
    MAX_NUMBER_OF_SHOWED_ELEMS = 10

    def __init__(self, slownik_nazwa_wartosc = dd()):
        self.lista_indeks_nazwa = list()
        self.slownik_nazwa_wartosc = slownik_nazwa_wartosc
        
    def __setitem__(self, nazwa, wartosc, zbior = False):
        if nazwa in self.lista_indeks_nazwa:
            raise ValueError(f"Obiekt matematyczny o danej nazwie już istnieje w {'zbiorze' if zbior else 'historii'}")
        self.lista_indeks_nazwa.append(nazwa) 
        self.slownik_nazwa_wartosc[nazwa] = wartosc

    def create_name(self):
        clear_terminal()               
        while(True):
            print("Podaj nazwę")
            user_input = input()
            if user_input == "":
                invalid_input("Podano nieprawidłową nazwę")
                continue
            if user_input in self.lista_indeks_nazwa:
                invalid_input("Obiekt matematyczny o danej nazwie już istnieje")
                continue
            return user_input
        
    def __getitem__(self, ind):
        return Historia.get_val(self.lista_indeks_nazwa[ind-1])


    def get_val(self, nazwa):
        return self.slownik_nazwa_wartosc[nazwa]
    
    def print_range(self, b, e, chosen=0, naglowek = "HISTORIA", color=Fore.GREEN):
        if b - e > Historia.MAX_NUMBER_OF_SHOWED_ELEMS:
            e = b + Historia.MAX_NUMBER_OF_SHOWED_ELEMS
        if e > len(self.lista_indeks_nazwa):
            e = len(self.lista_indeks_nazwa)
        clear_terminal()
        print("---------", naglowek, "-----------")
        max_len = len(str(e))
        for i in range(b-1, e):
            obiekt = self.slownik_nazwa_wartosc[self.lista_indeks_nazwa[i]]
            print(f"{Fore.YELLOW}{i+1}: {Style.RESET_ALL}", end="")
            print(" " * (max_len - len(str(i+1))), end="")
            print(f"{Fore.CYAN}{self.print_type_repr(obiekt)} {Style.RESET_ALL}", end="")
            if i != chosen - 1: 
                print(repr(obiekt))
            else:
                print(f"{color}{repr(obiekt)}{Style.RESET_ALL}")



    def browse_history(self):
        i = 1
        chosen = 1
        while True:
            self.print_range(i, i + self.MAX_NUMBER_OF_SHOWED_ELEMS - 1, chosen)
            print("Używaj ws, aby poruszać się po historii")
            print("Naciśnij ENTER jeśli chcesz zobaczyć wartość w wybranym polu")
            print("Naciśnij q jeśli chcesz zakończyć przeglądanie historii")
            user_input = get_char()
            if user_input == "enter":
                self.show_object(chosen)
            elif user_input == "w":
                if chosen - 1 < i:
                    if i > 1:
                        i -= 1
                        chosen -= 1
                else:
                    chosen -= 1
            elif user_input == "s":
                if chosen + 1 > i + self.MAX_NUMBER_OF_SHOWED_ELEMS - 1:
                    if i + self.MAX_NUMBER_OF_SHOWED_ELEMS - 1 < len(self.lista_indeks_nazwa):
                        i += 1
                        chosen += 1
                else:
                    chosen += 1
            elif user_input == "q":
                break
            else:
                invalid_input("Podano nieprawidłową wartość")       
            
    def print_all(self):
        Historia.print_range(self, 1, self.dlugosc_historii)
        
    def display_memory_menu():
        clear_terminal()
        print("------------MENU-PAMIĘCI---------------")
        print("1. Zapisane obiekty matematyczne")
        print("2. Zapisane operacje")
        print("3. Menu Główne")
        print("Podaj liczbę:   ", end="")
        
        

        
