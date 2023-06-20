
from historia import Historia
from colorama import Fore, Style

from aux import clear_terminal, invalid_input
from obiekt_matematyczny import ObiektMatematyczny
from macierz import Macierz
from wektor import Wektor
from liczba import Liczba
from stala import Stala
from zmienna import Zmienna
from zbior import Zbior

class HistoriaObiektow(Historia):
    def __init__(self):
        Historia.__init__(self)

    def display_add_object_memory_menu():
        clear_terminal()
        print("Czy chcesz dodać obiekt do historii?")
        print("1. Dodaj do pamięci")
        print("2. Usuń obiekt")
        print("Podaj liczbę:   ", end="")   
    
    def add_to_history(self, operacja):
        while (True):
            HistoriaObiektow.display_add_object_memory_menu()
            user_input = input()
            if (user_input == "1"):
                obiekt = operacja.get_result()
                if not isinstance(obiekt, Liczba):
                    nazwa = self.create_name()
                    obiekt.set_name(nazwa)
                    self[nazwa] = obiekt
                else:
                    self[str(obiekt)] = obiekt
                break
            elif (user_input == "2"):
                break
            else:
                invalid_input("Podano niepoprawne dane") 
        
    def show_object(self, i, wait=True, mode="show_object"):
        object = self.slownik_nazwa_wartosc[self.lista_indeks_nazwa[i-1]]
        if not isinstance(object, Zbior):
            if not isinstance(object, Liczba) or isinstance(object, Stala) or isinstance(object, Zmienna):
                print(repr(object))
            print(object)
            if wait:
                user_input = input()
        else:
            if mode != "return_object":
                object.browse_set()
        
    def display_object_memory_menu():
        clear_terminal()
        print("------------HISTORIA-OBIEKTÓW---------------")
        print("1. Nowa macierz")
        print("2. Nowy wektor")
        print("3. Nowa liczba")
        print("4. Nowa stała")
        print("5. Nowa zmienna")
        print("6. Nowy zbior")
        print("7. Usuń wybrany obiekt")
        print("8. Przeglądaj zapisane obiekty matematyczne")
        print("9. Edytuj wybrany obiekt")
        print("10. Menu Pamięci")
        print("Podaj liczbę:   ", end="")
        
    def object_memory_menu(self):
        while (True):
            HistoriaObiektow.display_object_memory_menu()
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
                self.new_set()
            elif (user_input == "7"):
                self.browse_history("remove_object")
            elif (user_input == "8"):
                self.browse_history("show_object")
            elif (user_input == "9"):
                object_to_mod = self.browse_history("return_object")
                if object_to_mod != None:
                    object_to_mod.modify()
            elif (user_input == "10"):
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