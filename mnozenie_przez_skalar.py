import numpy as np
from aux import clear_terminal
from operacja_unarna import OperacjaUnarna
from operacja_binarna import OperacjaBinarna
from macierz import Macierz

class MnozeniePrzezSkalar(OperacjaBinarna):
    nazwa_typu = "DODAWANIE"
    def __init__(self, nazwa, num, m1):
        OperacjaUnarna.__init__(self, nazwa, m1)
        self.m = self.wymiary1[0]
        self.n = self.wymiary1[1]
        self.num = num
        
    def enter_num_m(historia, nazwa = ""):
        clear_terminal()
        print("Podaj skalar")
        num = OperacjaUnarna.enter_number(historia)
        clear_terminal()
        print("Podaj drugą macierz")
        m1 = OperacjaUnarna.enter_matrix(historia)
        return MnozeniePrzezSkalar(nazwa, num, m1)
    
    def run_operation(self):
        my_list = [[] for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                my_list[i].append(str(self.num.get_value()) + "*" + str(self.m1[i+1, j+1]))

        t1 = np.array(my_list, dtype=np.str_)
        step1 = Macierz(self.m, self.n, "", t1)
        
        self.lista_krokow.append(OperacjaBinarna.str_num_op_m_eq_m(self.num, self.m1, step1, "*"))
        step1.eval()
        self.lista_krokow.append(OperacjaBinarna.str_num_op_m_eq_m(self.num, self.m1, step1, "*"))
        self.result = step1