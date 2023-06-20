
from collections import defaultdict as dd
from colorama import Fore, Style

from aux import *

class Historia:
    MAX_NUMBER_OF_SHOWED_ELEMS = 10

    def __init__(self, slownik_nazwa_wartosc = dd()):
        self.lista_indeks_nazwa = list()
        self.slownik_nazwa_wartosc = slownik_nazwa_wartosc
        self.dlugosc_historii = lambda : len(self.lista_indeks_nazwa)
        
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
            try:
                user_input = int(user_input)
                invalid_input("Podano nieprawidłową nazwę")
                continue
            except:
                if user_input in self.lista_indeks_nazwa:
                    invalid_input("Obiekt matematyczny o danej nazwie już istnieje")
                    continue
                return user_input
        
    def __getitem__(self, nazwa_ind):
        if nazwa_ind in self.lista_indeks_nazwa:
            return self.slownik_nazwa_wartosc[nazwa_ind]
        try:
            ind = int(nazwa_ind)
        except:
            invalid_input("Obiekt o danej nazwie nie istnieje")
        return self.get_val(self.lista_indeks_nazwa[ind-1])
    
    def remove(self, nazwa):
        self.lista_indeks_nazwa.remove(nazwa)
        self.slownik_nazwa_wartosc.pop(nazwa)

    def get_val(self, nazwa):
        return self.slownik_nazwa_wartosc[nazwa]
    
    def print_range(self, b, e, chosen=0, naglowek = "HISTORIA", color=Fore.GREEN):
        if b - e > Historia.MAX_NUMBER_OF_SHOWED_ELEMS:
            e = b + Historia.MAX_NUMBER_OF_SHOWED_ELEMS
        if e > self.dlugosc_historii():
            e = self.dlugosc_historii()
        clear_terminal()
        print("---------", naglowek, "-----------")
        max_len = len(str(e))
        max_len_type_repr = len(max([obiekt.type_repr() for obiekt 
                                 in self.slownik_nazwa_wartosc.values()], key=len))
        for i in range(b-1, e):
            obiekt = self.slownik_nazwa_wartosc[self.lista_indeks_nazwa[i]]
            print(f"{Fore.YELLOW}{i+1}: {Style.RESET_ALL}", end="")
            print(" " * (max_len - len(str(i+1))), end="")
            print(f"{Fore.CYAN}{obiekt.type_repr()} {Style.RESET_ALL}", end="")
            print(" " * (max_len_type_repr - len(obiekt.type_repr())), end="")
            if i != chosen - 1: 
                print(repr(obiekt))
            else:
                print(f"{color}{repr(obiekt)}{Style.RESET_ALL}")

    def browse_history(self, mode="show_object"):
        i = 1
        chosen = 1
        while True:
            self.print_range(i, i + self.MAX_NUMBER_OF_SHOWED_ELEMS - 1, chosen)
            print("Używaj ws, aby poruszać się po historii")
            print("Naciśnij ENTER jeśli chcesz zobaczyć wartość w wybranym polu")
            print("Naciśnij q jeśli chcesz zakończyć przeglądanie historii")
            user_input = get_char()
            if user_input == "enter":
                if mode == "show_object":
                    self.show_object(chosen)
                elif mode == "return_object":
                    res = self.return_menu(chosen)
                    if res != None:
                        return res
                elif mode == "remove_object":
                    if self.dlugosc_historii() > 0:
                        self.delete_menu(chosen)
                        if chosen > self.dlugosc_historii():
                            chosen -= 1
                    else:
                        invalid_input("Historia jest pusta")
            elif user_input == "w":
                if chosen - 1 < i:
                    if i > 1:
                        i -= 1
                        chosen -= 1
                else:
                    chosen -= 1
            elif user_input == "s":
                if chosen >= self.dlugosc_historii():
                    continue
                if chosen + 1 > i + self.MAX_NUMBER_OF_SHOWED_ELEMS - 1:
                    if i + self.MAX_NUMBER_OF_SHOWED_ELEMS - 1 < self.dlugosc_historii():
                        i += 1
                        chosen += 1
                else:
                    chosen += 1
            elif user_input == "q":
                break
    
    def return_object_memory_menu():
        print("Czy chcesz wybrać podany obiekt?")
        print("1. Tak")
        print("2. Wybierz inny")
        print("Podaj liczbę:   ", end="")
    
    def return_menu(self, chosen):
        while True:
            self.show_object(chosen, wait=False, mode="return_object")
            Historia.return_object_memory_menu()
            user_input = input()
            if (user_input == "1"):
                return self[chosen]
            elif (user_input == "2"):
                return None
            else:
                invalid_input("Podano niepoprawne dane") 

    def delete_object_memory_menu():
        print("Czy chcesz usunąć podany obiekt?")
        print("1. Tak")
        print("2. Wybierz inny")
        print("Podaj liczbę:   ", end="")
    
    def delete_menu(self, chosen):
        while True:
            self.show_object(chosen)
            Historia.delete_object_memory_menu()
            user_input = input()
            if (user_input == "1"):
                self.remove(self.lista_indeks_nazwa[chosen-1])
                break
            elif (user_input == "2"):
                break
            else:
                invalid_input("Podano niepoprawne dane")   
                
    def return_from_history(self):
        return self.browse_history(mode="return_object")
            
    def print_all(self):
        Historia.print_range(self, 1, self.dlugosc_historii())
        
    def display_memory_menu():
        clear_terminal()
        print("------------MENU-PAMIĘCI---------------")
        print("1. Zapisane obiekty matematyczne")
        print("2. Zapisane operacje")
        print("3. Menu Główne")
        print("Podaj liczbę:   ", end="")
        
        

        
