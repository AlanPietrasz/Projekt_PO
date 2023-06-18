
from collections import defaultdict as dd
from colorama import Fore, Style


from macierz import Macierz
from wektor import Wektor
from liczba import Liczba
from stala import Stala
from zmienna import Zmienna
from zbior import Zbior
from aux import clear_terminal, get_char

class Historia:
    MAX_NUMBER_OF_SHOWED_ELEMS = 10

    
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

    def print_type_repr(obiekt):
        if isinstance(obiekt, Zmienna):
            return "Zmienna "
        elif isinstance(obiekt, Stala):
            return "Stała   "
        elif isinstance(obiekt, Liczba):
            return "Liczba  "
        elif isinstance(obiekt, Zbior):
            return "Zbiór   "       
        elif isinstance(obiekt, Wektor):
            return "Wektor  "  
        elif isinstance(obiekt, Macierz):
            return "Macierz "  
        
    def get_val(self, nazwa):
        return self.slownik_nazwa_wartosc[nazwa]
    
    def show_object(self, i):
        object = self.slownik_nazwa_wartosc[self.slownik_indeks_klucz[i-1]]
        if not isinstance(object, Zbior):
            if not isinstance(object, Liczba) or isinstance(object, Stala) or isinstance(object, Zmienna):
                print(repr(object))
            print(object)
        else:
            object.browse_set()
        user_input = input()

        
    
    def print_range(self, b, e, chosen=0, color=Fore.GREEN):
        if b - e > Historia.MAX_NUMBER_OF_SHOWED_ELEMS:
            e = b + Historia.MAX_NUMBER_OF_SHOWED_ELEMS
        if e > self.dlugosc_historii:
            e = self.dlugosc_historii
        clear_terminal()
        print("---------HISTORIA-----------")
        max_len = len(str(e))
        for i in range(b-1, e):
            obiekt = self.slownik_nazwa_wartosc[self.slownik_indeks_klucz[i]]
            print(f"{Fore.YELLOW}{i+1}: {Style.RESET_ALL}", end="")
            print(" " * (max_len - len(str(i+1))), end="")
            print(f"{Fore.CYAN}{Historia.print_type_repr(obiekt)} {Style.RESET_ALL}", end="")
            if i != chosen - 1: 
                print(repr(obiekt))
            else:
                print(f"{color}{repr(obiekt)}{Style.RESET_ALL}")


    def browse_history(self):
        i = 1
        chosen = 1
        while True:
            self.print_range(i, i + self.MAX_NUMBER_OF_SHOWED_ELEMS, chosen)
            print("Używaj ws, aby poruszać się po historii")
            print("Naciśnij ENTER jeśli chcesz zobaczyć wartość w wybranym polu")
            print("Naciśnij q jeśli chcesz zakończyć przeglądanie historii")
            user_input = get_char()
            if user_input == "enter":
                self.show_object(chosen)
            elif user_input == "w":
                # if chosen == 1:
                #     continue
                if chosen - 1 < i:
                    if i > 1:
                        i -= 1
                        chosen -= 1
                else:
                    chosen -= 1

            elif user_input == "s":
                # if i < self.dlugosc_historii:
                #     i += 1
                # if chosen == self.dlugosc_historii:
                #     continue
                if chosen + 1 > i + self.MAX_NUMBER_OF_SHOWED_ELEMS:
                    if i + self.MAX_NUMBER_OF_SHOWED_ELEMS < self.dlugosc_historii:
                        i += 1
                        chosen += 1
                else:
                    chosen += 1
            elif user_input == "q":
                break
            else:
                print("Podano nieprawidłową wartość")
                user_input = input()
        
    
    def update_len(self):
        self.dlugosc_historii = len(self.slownik_indeks_klucz)        
            
    def print_all(self):
        Historia.print_range(self, 1, self.dlugosc_historii)