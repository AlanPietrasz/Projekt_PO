
from aux import invalid_input, clear_terminal
from operacja import Operacja
from macierz import Macierz
from historia import Historia

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
           

           
    def enter_matrix(historia, m = 0, n = 0):
        while True:
            OperacjaUnarna.display_enter_matrix_menu()
            user_input = input()
            if (user_input == "1"):
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
            