
import numpy as np

from macierz import Macierz

from operacja_binarna import OperacjaBinarna

class Dodawanie(OperacjaBinarna):
    nazwa_operacji = "DODAWANIE"
    def __init__(self, nazwa, m1, m2):
        OperacjaBinarna.__init__(self, nazwa, m1, m2)
        if self.wymiary1 != self.wymiary2:
            raise ValueError("Wymiary macierzy nie są takie same")
        self.m = self.wymiary1[0]
        self.n = self.wymiary1[1]

        
    def run_operation(self):
        my_list = [[] for _ in range(self.m)]
        for i in range(self.m):
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
        
    