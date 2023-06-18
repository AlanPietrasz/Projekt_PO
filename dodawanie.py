from aux import clear_terminal, get_char
import numpy as np

from macierz import Macierz

from operacja import Operacja

class Dodawanie(Operacja):
    def __init__(self, nazwa, m1, m2):
        self.nazwa = nazwa
        self.m1 = m1
        self.m2 = m2
        wymiary1 = m1.get_dimensions()
        wymiary2 = m2.get_dimensions()
        if wymiary1 != wymiary2:
            raise ValueError("Wymiary macierzy nie są takie same")
        self.m = wymiary1[0]
        self.n = wymiary1[1]
        self.lista_krokow = []
        self.liczba_krokow = len(self.lista_krokow)
        
    def run_operation(self):
        v1 = self.m1.get_value()
        v2 = self.m2.get_value()
        my_list = [[] for _ in range(self.m)]
        for i in range(self.m):
            #my_list.append([])
            for j in range(self.n):
                print(my_list)
                my_list[i].append(str(self.m1[i+1, j+1]) + "+" + str(self.m2[i+1, j+1]))

        t1 = np.array(my_list, dtype=np.str_)
        step1 = Macierz(self.m, self.n, "", t1)
        self.lista_krokow.append(str(step1))
        step1.eval()
        print(step1)
        self.lista_krokow.append(str(step1))
        self.update_liczba_krokow()
        
    def update_liczba_krokow(self):
        self.liczba_krokow = len(self.lista_krokow)
        
    def print_operation_steps(self):
        if self.lista_krokow == []:
            self.run_operation()
        i = 0
        while True:
            clear_terminal()
            print("DODAWANIE: ")
            print(self.lista_krokow[i])
            print("Używaj ad, aby poruszać się po krokach operacji")
            print("Naciśnij q jeśli chcesz zakończyć przeglądanie kroków operacji")
            user_input = get_char()
            print(i)
            # if user_input == "enter":
            #     self.show_object(chosen)
            if user_input == "a":
                # if chosen == 1:
                #     continue
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
        
    