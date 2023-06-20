
from aux import invalid_input, clear_terminal
from operacja import Operacja
from macierz import Macierz
from historia import Historia
from obiekt_matematyczny import ObiektMatematyczny
from liczba import Liczba
from stala import Stala
from zmienna import Zmienna

class OperacjaUnarna(Operacja):
    def __init__(self, nazwa, m1):
        Operacja.__init__(self, nazwa)
        self.m1 = m1
        self.wymiary1 = m1.get_dimensions()
        
    def display_enter_matrix_menu():
        #clear_terminal()
        print("------------WYBIERZ-MACIERZ---------------") 
        print("1. Utwórz nową macierz")
        print("2. Wybierz macierz z pamięci")       
        print("Podaj liczbę:   ", end="")
 
    def display_enter_number_menu():
        #clear_terminal()
        print("------------WYBIERZ-SKALAR---------------") 
        print("1. Utwórz nową liczbę")
        print("2. Wybierz liczbę z pamięci")       
        print("Podaj liczbę:   ", end="")          

           
    def enter_matrix(historia, m = 0, n = 0, equal=False):
        while True:
            OperacjaUnarna.display_enter_matrix_menu()
            user_input = input()
            if (user_input == "1"):
                if equal:
                    return Macierz.create_matrix("", m, n, equal)
                else:
                    return Macierz.create_matrix("", m, n)
            elif (user_input == "2"):
                obiekt = historia.return_from_history()
                if isinstance(obiekt, Macierz): 
                    if obiekt.eq_dimensions(m, n):
                        return obiekt
                    else:
                        invalid_input("Wybrana macierz ma nieodpowiednie wymiary")
                else:
                    invalid_input("Wybrano obiekt innego typu niż macierz")
            else:
                invalid_input("Podano niepoprawne dane")
                
    def enter_number(historia):
        while True:
            OperacjaUnarna.display_enter_number_menu()
            user_input = input()
            if (user_input == "1"):
                return Liczba(ObiektMatematyczny.create_number_val())
            elif (user_input == "2"):
                obiekt = historia.return_from_history()
                if isinstance(obiekt, Liczba) or isinstance(obiekt, Stala) or isinstance(obiekt, Zmienna):
                    return obiekt
                else:
                    invalid_input("Wybrano obiekt innego typu niż liczba, stała lub zmienna")
            else:
                invalid_input("Podano niepoprawne dane")
            