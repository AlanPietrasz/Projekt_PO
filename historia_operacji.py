
from historia import Historia

from aux import clear_terminal, invalid_input
from operacja import Operacja
from dodawanie import Dodawanie

class HistoriaOperacji(Historia):
    def __init__(self):
        Historia.__init__(self)
        
    # def type_repr(self, obiekt):
    #     return obiekt.nazwa_typu
        # if isinstance(obiekt, Dodawanie):
        #     return "Zmienna "
        # elif isinstance(obiekt, Stala):
        #     return "Stała   "
        # elif isinstance(obiekt, Liczba):
        #     return "Liczba  "
        # elif isinstance(obiekt, Zbior):
        #     return "Zbiór   "       
        # elif isinstance(obiekt, Wektor):
        #     return "Wektor  "  
        # elif isinstance(obiekt, Macierz):
        #     return "Macierz "  
    
    def display_operation_memory_menu():
        clear_terminal()
        print("------------HISTORIA-OPERACJI---------------")
        print("1. Przeglądaj zapisane obiekty matematyczne")
        print("2. Menu Pamięci")
        print("Podaj liczbę:   ", end="")   
    
        
    def operation_memory_menu(self):
        while (True):
            HistoriaOperacji.display_operation_memory_menu()
            user_input = input()
            if (user_input == "1"):
                self.browse_history()
            elif (user_input == "2"):
                break
            else:
                invalid_input("Podano niepoprawne dane")
     
    def show_object(self, chosen):
        self[chosen].print_operation_steps()