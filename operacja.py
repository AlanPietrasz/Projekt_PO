from aux import clear_terminal, get_char

import numpy as np

class Operacja:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.lista_krokow = []
        self.result = None
    
    def set_name(self, nazwa):
        self.nazwa = nazwa

    def print_and_save(self, menu):
        self.print_operation_steps()
        menu.historia_operacji.add_to_history(self)
        menu.historia_obiektow.add_to_history(self)   
        
    
    def type_repr(self):
        return self.nazwa_typu
    
    def get_result(self):
        if self.result != None:
            return self.result
        else:
            self.run_operation()
            return self.result
    
    def __repr__(self):
        return self.nazwa
    
    def get_steps(self):
        if self.lista_krokow == []:
            self.run_operation()
        return self.lista_krokow
        
    def print_operation_steps(self):
        if self.lista_krokow == []:
            self.run_operation()
        i = 0
        while True:
            clear_terminal()
            print(self.nazwa_typu, ": ")
            print("Krok: ", i+1)
            print(self.lista_krokow[i])
            print("Używaj ad, aby poruszać się po krokach operacji")
            print("Naciśnij q jeśli chcesz zakończyć przeglądanie kroków operacji")
            user_input = get_char()
            print(i)
            if user_input == "a":
                if i > 0:
                    i -= 1
            elif user_input == "d":
                if i < len(self.lista_krokow) -1:
                    i += 1
            elif user_input == "q":
                break
            else:
                print("Podano nieprawidłową wartość")
                user_input = input()
                
    def print_all_operation_steps(self):
        clear_terminal()
        print(self.nazwa_operacji, ": ")
        for i, e in enumerate(self.lista_krokow):
            print("Krok: ", i+1)
            print(e)