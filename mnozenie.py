
import numpy as np

from aux import clear_terminal
from macierz import Macierz

from operacja_unarna import OperacjaUnarna
from operacja_binarna import OperacjaBinarna

class Mnozenie(OperacjaBinarna):
    nazwa_typu = "MNOŻENIE"
    def __init__(self, nazwa, m1, m2):
        OperacjaBinarna.__init__(self, nazwa, m1, m2)
        if self.wymiary1[1] != self.wymiary2[0]:
            raise ValueError("Wymiary macierzy nie są takie same")
        self.m = self.wymiary1[0]
        self.n = self.wymiary1[1]
        self.k = self.wymiary2[1]

    def enter_m_m(historia, nazwa = ""):
        clear_terminal()
        print("Podaj pierwszą macierz")
        m1 = OperacjaUnarna.enter_matrix(historia)
        clear_terminal()
        print("Podaj drugą macierz")
        m2 = OperacjaUnarna.enter_matrix(historia, m1.get_dimensions()[1])
        return Mnozenie(nazwa, m1, m2)
        
    def run_operation(self):
        res_matrix = Macierz(self.m, self.k)
        for i in range(1, self.m+1):
            for j in range(1, self.k+1):
                color_list1 = [(i, l) for l in range(1, self.n+1)]
                color_list2 = [(l, j) for l in range(1, self.n+1)]
                res_str = "+".join([str(self.m1[i, l]) + "*" + str(self.m2[l, j]) for l in range(1, self.n+1)])
                res_matrix[i, j] = res_str
                self.lista_krokow.append(OperacjaBinarna.str_m_op_m_eq_m(self.m1, self.m2, res_matrix, "*", color_list1, color_list2, [(i, j)]))
                res_matrix[i, j] = eval(res_str)
                self.lista_krokow.append(OperacjaBinarna.str_m_op_m_eq_m(self.m1, self.m2, res_matrix, "*", color_list1, color_list2, [(i, j)]))

        self.result = res_matrix
        
    