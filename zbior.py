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
      

    def modify(self):
        self.set_menu()
    
    def show_object(self, i, wait=True, mode="show_object"):
        object = self.slownik_nazwa_wartosc[self.lista_indeks_nazwa[i-1]]
        if not isinstance(object, Liczba) or isinstance(object, Stala) or isinstance(object, Zmienna):
            print("Nazwa obiektu:")
            print(repr(object))
        print("Wartość")
        print(object)
        if wait:
            user_input = input()
        
    def print_range(self, b, e, chosen=0, naglowek = "ZBIÓR", color=Fore.GREEN):
        Historia.print_range(self, b, e, chosen, naglowek, color)

    def browse_set(self, mode="show_object"):
        return self.browse_history(mode)
    
    def display_set_menu():
        clear_terminal()
        print("------------MENU-ZBIORU---------------")
        print("1. Nowa macierz")
        print("2. Nowy wektor")
        print("3. Nowa liczba")
        print("4. Nowa stała")
        print("5. Nowa zmienna")
        print("6. Usuń wybrany obiekt")
        print("7. Przeglądaj zapisane obiekty matematyczne")
        print("8. Edytuj wybrany obiekt")
        print("9. Menu historii obiektów")
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
                self.browse_history("remove_object")
            elif (user_input == "7"):
                self.browse_history("show_object")
            elif (user_input == "8"):
                object_to_mod = self.browse_history("return_object")
                if object_to_mod != None:
                    object_to_mod.modify()
            elif (user_input == "9"):
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