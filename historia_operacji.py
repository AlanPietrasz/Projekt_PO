
from historia import Historia

from aux import clear_terminal, invalid_input
from operacja import Operacja
from dodawanie import Dodawanie

class HistoriaOperacji(Historia):
    def __init__(self):
        Historia.__init__(self)
        
    def display_add_operation_memory_menu():
        clear_terminal()
        print("Czy chcesz dodać operację do historii?")
        print("1. Dodaj do pamięci")
        print("2. Usuń operację")
        print("Podaj liczbę:   ", end="")   
    
    def add_to_history(self, operacja):
        while (True):
            HistoriaOperacji.display_add_operation_memory_menu()
            user_input = input()
            if (user_input == "1"):
                nazwa = self.create_name()
                operacja.set_name(nazwa)
                self[nazwa] = operacja
                break
            elif (user_input == "2"):
                break
            else:
                invalid_input("Podano niepoprawne dane")        

    def display_operation_memory_menu():
        clear_terminal()
        print("------------HISTORIA-OPERACJI---------------")
        print("1. Przeglądaj zapisane operacje")
        print("2. Usuń wybraną operację z pamięci")
        print("3. Menu Pamięci")
        print("Podaj liczbę:   ", end="")   
    
        
    def operation_memory_menu(self):
        while (True):
            HistoriaOperacji.display_operation_memory_menu()
            user_input = input()
            if (user_input == "1"):
                self.browse_history()
            elif (user_input == "2"):
                self.browse_history("remove_object")
            elif (user_input == "3"):
                break
            else:
                invalid_input("Podano niepoprawne dane")
     
    def show_object(self, chosen, wait=True, mode="show_object"):
        if isinstance(self[chosen], HistoriaOperacji):
            self[chosen].browse_history(mode)
        else:
            self[chosen].print_operation_steps()