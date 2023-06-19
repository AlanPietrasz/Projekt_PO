
from colorama import Fore
import numpy as np

from macierz import Macierz

from operacja_binarna import OperacjaBinarna

class Dodawanie(OperacjaBinarna):
    nazwa_typu = "DODAWANIE"
    def __init__(self, nazwa, m1, m2):
        OperacjaBinarna.__init__(self, nazwa, m1, m2)
        if self.wymiary1 != self.wymiary2:
            raise ValueError("Wymiary macierzy nie są takie same")
        self.m = self.wymiary1[0]
        self.n = self.wymiary1[1]
        
    def str_m_op_m_eq_m(self, other, other2, operator="+", color_list1=[], color_list2=[], color_list3=[], color=Fore.GREEN, color2=Fore.CYAN):
        return super().str_m_op_m_eq_m(other, other2, operator, color_list1, color_list2, color_list3, color, color2)
        
    def run_operation(self):
        my_list = [[] for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                my_list[i].append(str(self.m1[i+1, j+1]) + "+" + str(self.m2[i+1, j+1]))

        t1 = np.array(my_list, dtype=np.str_)
        step1 = Macierz(self.m, self.n, "", t1)
        
        self.lista_krokow.append(OperacjaBinarna.str_m_op_m_eq_m(self.m1, self.m2, step1))
        step1.eval()
        self.lista_krokow.append(OperacjaBinarna.str_m_op_m_eq_m(self.m1, self.m2, step1))
        self.result = step1