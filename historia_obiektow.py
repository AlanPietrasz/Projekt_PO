
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
        
    def show_object(self, i):
        object = self.slownik_nazwa_wartosc[self.lista_indeks_nazwa[i-1]]
        if not isinstance(object, Zbior):
            if not isinstance(object, Liczba) or isinstance(object, Stala) or isinstance(object, Zmienna):
                print(repr(object))
            print(object)
            user_input = input()
        else:
            object.browse_set()
        
    
    def print_type_repr(self, obiekt):
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
        
    def display_object_memory_menu():
        clear_terminal()
        print("------------HISTORIA-OBIEKTÓW---------------")
        print("1. Nowa macierz")
        print("2. Nowy wektor")
        print("3. Nowa liczba")
        print("4. Nowa stała")
        print("5. Nowa zmienna")
        print("6. Nowy zbior")
        print("7. Edytuj wybrany obiekt")
        print("8. Przeglądaj zapisane obiekty matematyczne")
        print("9. Menu Pamięci")
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
                pass
            elif (user_input == "8"):
                # self.historia_obiektow.print_all()
                self.browse_history()
                # user_input = input()
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