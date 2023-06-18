from aux import *
from collections import defaultdict as dd
from colorama import Fore, Style

from historia import Historia
from obiekt_matematyczny import ObiektMatematyczny
from macierz import Macierz
from wektor import Wektor
from liczba import Liczba
from stala import Stala
from zmienna import Zmienna

class Zbior(ObiektMatematyczny, Historia):
    MAX_NUMBER_OF_SHOWED_ELEMS = 10
    MAX_SET_LEN = 20
    
    def __init__(self, nazwa, slownik_nazwa_wartosc = dd()):
        self.nazwa = nazwa
        Historia.__init__(self, slownik_nazwa_wartosc)
        
        
    def __setitem__(self, nazwa, obiekt):
        if len(self.lista_indeks_nazwa) >= Zbior.MAX_SET_LEN:
            raise ValueError("Osiągnięto maksymalną liczbę obiektów matematycznych w danym zbiorze")
        else:
            Historia.__setitem__(self, nazwa, obiekt, zbior = True)
        
    def __getitem__(self, nazwa):
        return self.slownik_nazwa_wartosc[nazwa]
    

    def remove(self, nazwa):
        self.lista_indeks_nazwa.remove(nazwa)
        self.slownik_nazwa_wartosc.pop(nazwa)
        
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
        
    def show_object(self, i):
        object = self.slownik_nazwa_wartosc[self.lista_indeks_nazwa[i-1]]
        if not isinstance(object, Liczba) or isinstance(object, Stala) or isinstance(object, Zmienna):
            print(repr(object))
        print(object)
        user_input = input() 
        
    def print_range(self, b, e, chosen=0, color=Fore.GREEN):
        if b - e > Zbior.MAX_NUMBER_OF_SHOWED_ELEMS:
            e = b + Zbior.MAX_NUMBER_OF_SHOWED_ELEMS
        if e > self.set_len():
            e = self.set_len()
        clear_terminal()
        print("---------ZBIÓR-----------")
        print("Nazwa zbioru: ", self.nazwa)
        max_len = len(str(e))
        for i in range(b-1, e):
            obiekt = self.slownik_nazwa_wartosc[self.lista_indeks_nazwa[i]]
            print(f"{Fore.YELLOW}{i+1}: {Style.RESET_ALL}", end="")
            print(" " * (max_len - len(str(i+1))), end="")
            print(f"{Fore.CYAN}{Zbior.print_type_repr(obiekt)} {Style.RESET_ALL}", end="")
            if i != chosen - 1: 
                print(repr(obiekt))
            else:
                print(f"{color}{repr(obiekt)}{Style.RESET_ALL}")


    def browse_set(self):
        i = 1
        chosen = 1
        while True:
            self.print_range(i, i + self.MAX_NUMBER_OF_SHOWED_ELEMS - 1, chosen)
            print("Używaj ws, aby poruszać się po zbiorze")
            print("Naciśnij ENTER jeśli chcesz zobaczyć wartość w wybranym polu")
            print("Naciśnij q jeśli chcesz zakończyć przeglądanie zbioru")
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
                    if i + self.MAX_NUMBER_OF_SHOWED_ELEMS - 1 < self.set_len():
                        i += 1
                        chosen += 1
                else:
                    chosen += 1
            elif user_input == "q":
                break
            else:
                print("Podano nieprawidłową wartość")
                user_input = input()
        
    # def __setitem__(self, obiekt)
        
    # def __getitem__(self, nazwa)
    
    def display_set_menu():
        clear_terminal()
        print("------------MENU-ZBIORU---------------")
        print("1. Nowa macierz")
        print("2. Nowy wektor")
        print("3. Nowa liczba")
        print("4. Nowa stała")
        print("5. Nowa zmienna")
        print("6. Edytuj wybrany obiekt")
        print("7. Przeglądaj zapisane obiekty matematyczne")
        print("8. Menu historii obiektów")
        print("Podaj liczbę:   ", end="")
        
    def create_set(nazwa):
        zbior = Zbior(nazwa)
        zbior.set_menu()
        return zbior
    



    def set_menu(self):
        while True:
            Zbior.display_set_menu()
            user_input = input()
            if (user_input == "1"):
                self.new_matrix()
            elif (user_input == "2"):
                self.new_vector()
            elif (user_input == "3"):
                self.new_number()
            elif (user_input == "4"):
                self.new_constant()
            elif (user_input == "5"):
                self.new_variable()
            elif (user_input == "6"):
                pass
            elif (user_input == "7"):
                # self.historia_obiektow.print_all()
                self.browse_set()
                # user_input = input()
            elif (user_input == "8"):
                break
            else:
                invalid_input("Podano niepoprawne dane")
                
                
    def new_matrix(self):
        nazwa = ObiektMatematyczny.create_name()
        nowy_obiekt = Macierz.create_matrix(nazwa)
        self[repr(nowy_obiekt)] = nowy_obiekt

    def new_vector(self):
        nazwa = ObiektMatematyczny.create_name()
        nowy_obiekt = Wektor.create_wektor(nazwa)
        self[repr(nowy_obiekt)] = nowy_obiekt       
        
    def new_number(self):
        while True:
            wartosc = ObiektMatematyczny.create_number_val()
            nazwa = str(wartosc)
            if not ObiektMatematyczny.is_free_name(nazwa):
                print("Podana liczba jest już zapisana")
                user_input = input()
                clear_terminal()
                continue
            break
        nowy_obiekt = Liczba(wartosc)
        self[repr(nowy_obiekt)] = nowy_obiekt       
        
    def new_constant(self):
        nazwa = ObiektMatematyczny.create_name()
        wartosc = Liczba.create_number_val()
        self[nazwa] = Stala(wartosc, nazwa)
        
    def new_variable(self):
        nazwa = ObiektMatematyczny.create_name()
        wartosc = Liczba.create_number_val()
        self[nazwa] = Zmienna(wartosc, nazwa)