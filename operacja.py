from aux import clear_terminal, get_char

import numpy as np

class Operacja:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.lista_krokow = []
        self.liczba_krokow = len(self.lista_krokow)
        
    def update_liczba_krokow(self):
        self.liczba_krokow = len(self.lista_krokow)
        
        
       
    def print_operation_steps(self):
        if self.lista_krokow == []:
            self.run_operation()
        i = 0
        while True:
            clear_terminal()
            print(self.nazwa_operacji, ": ")
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
                if i < self.liczba_krokow -1:
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