
from colorama import Fore
import numpy as np

from aux import clear_terminal
from macierz import Macierz

from operacja_unarna import OperacjaUnarna
from operacja_binarna import OperacjaBinarna

class Dodawanie(OperacjaBinarna):
    nazwa_typu = "DODAWANIE"
    def __init__(self, nazwa, m1, m2):
        OperacjaBinarna.__init__(self, nazwa, m1, m2)
        if self.wymiary1 != self.wymiary2:
            raise ValueError("Wymiary macierzy nie są takie same")
        self.m = self.wymiary1[0]
        self.n = self.wymiary1[1]
        
    def enter_m_m(historia, nazwa = ""):
        clear_terminal()
        print("Podaj pierwszą macierz")
        m1 = OperacjaUnarna.enter_matrix(historia)
        clear_terminal()
        print("Podaj drugą macierz")
        m2 = OperacjaUnarna.enter_matrix(historia, m1.get_dimensions()[0], m1.get_dimensions()[1])
        return Dodawanie(nazwa, m1, m2)
      
    def run_operation(self):
        my_list = [[] for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                my_list[i].append(str(self.m1[i+1, j+1]) + "+" + str(self.m2[i+1, j+1]))

        t1 = np.array(my_list, dtype=np.str_)
        step1 = Macierz(self.m, self.n, "", t1)
        
        self.lista_krokow.append(OperacjaBinarna.str_m_op_m_eq_m(self.m1, self.m2, step1, "+"))
        step1.eval()
        self.lista_krokow.append(OperacjaBinarna.str_m_op_m_eq_m(self.m1, self.m2, step1, "+"))
        self.result = step1