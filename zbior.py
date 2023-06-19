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
    nazwa_typu = "ZBIÓR"
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
        
    # def __getitem__(self, nazwa):
    #     Historia.__getitem__(self, nazwa)
        
    # def type_repr(self, obiekt):
    #     if isinstance(obiekt, Zmienna):
    #         return "Zmienna "
    #     elif isinstance(obiekt, Stala):
    #         return "Stała   "
    #     elif isinstance(obiekt, Liczba):
    #         return "Liczba  "
    #     elif isinstance(obiekt, Zbior):
    #         return "Zbiór   "
    #     elif isinstance(obiekt, Wektor):
    #         return "Wektor  "
    #     elif isinstance(obiekt, Macierz):
    #         return "Macierz "
    
    def show_object(self, i):
        object = self.slownik_nazwa_wartosc[self.lista_indeks_nazwa[i-1]]
        if not isinstance(object, Liczba) or isinstance(object, Stala) or isinstance(object, Zmienna):
            print(repr(object))
        print(object)
        user_input = input() 
        
    def print_range(self, b, e, chosen=0, naglowek = "ZBIÓR", color=Fore.GREEN):
        Historia.print_range(self, b, e, chosen, naglowek, color)


    def browse_set(self):
        Historia.browse_history(self)
        
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
                self.browse_set()
            elif (user_input == "8"):
                break
            else:
                invalid_input("Podano niepoprawne dane")
    
    def new_matrix(self):
        nazwa = self.create_name()
        nowy_obiekt = Macierz.create_matrix(nazwa)
        self[repr(nowy_obiekt)] = nowy_obiekt

    def new_vector(self):
        nazwa = self.create_name()
        nowy_obiekt = Wektor.create_wektor(nazwa)
        self[repr(nowy_obiekt)] = nowy_obiekt
        
    def new_number(self):
        while True:
            wartosc = ObiektMatematyczny.create_number_val()
            nazwa = str(wartosc)
            if nazwa in self.lista_indeks_nazwa:
                invalid_input("Podana liczba jest już zapisana")
                continue
            break
        nowy_obiekt = Liczba(wartosc)
        self[repr(nowy_obiekt)] = nowy_obiekt
        
    def new_constant(self):
        nazwa = self.create_name()
        wartosc = Liczba.create_number_val()
        self[nazwa] = Stala(wartosc, nazwa)
        
    def new_variable(self):
        nazwa = self.create_name()
        wartosc = Liczba.create_number_val()
        self[nazwa] = Zmienna(wartosc, nazwa)
        
    def new_set(self):
        nazwa = self.create_name()
        nowy_obiekt = Zbior.create_set(nazwa)
        self[nazwa] = nowy_obiekt