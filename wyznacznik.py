import copy
from aux import clear_terminal

from liczba import Liczba
from operacja_unarna import OperacjaUnarna
from eliminacja_gaussa import EliminacjaGaussa
from mnozenie_przez_skalar import MnozeniePrzezSkalar

class Wyznacznik(EliminacjaGaussa):
    nazwa_typu = "WYZNACZNIK"
    def __init__(self, nazwa, m1):
        OperacjaUnarna.__init__(self, nazwa, m1)
        if self.wymiary1[0] != self.wymiary1[1]:
            raise ValueError("Macierz nie jest kwadratowa")
        self.m = self.wymiary1[0]
        self.n = self.wymiary1[1]
        self.result_matrix = None
        self.steps_without_det = None
    
    def get_result_matrix(self):
        while self.result_matrix == None:
            self.run_operation()
        return self.result_matrix
            
    def get_steps_without_det(self):
        if self.steps_without_det == None:
            self.run_operation()
        return self.steps_without_det
    
    def enter_m(historia, nazwa = ""):
        clear_terminal()
        print("Podaj macierz")
        m1 = OperacjaUnarna.enter_matrix(historia, 0, 0, True)
        return Wyznacznik(nazwa, m1)
    
    def run_operation(self):
        EliminacjaGaussa.run_operation(self)
        if self.licznik_zamiany_kolumn % 2 == 1:
            res = MnozeniePrzezSkalar("", Liczba(-1), self.get_result())
            self.lista_krokow += res.get_steps()
        else:
            res = MnozeniePrzezSkalar("", Liczba(1), self.get_result())
        res_matrix = res.get_result()
        color_list1 = [(l, l) for l in range(1, self.n+1)]
        self.steps_without_det = copy.copy(self.lista_krokow)
        self.lista_krokow.append(res_matrix.to_str(color_list1))
        res_str = ""
        for i in range(1, self.n+1):
            res_str += str(res_matrix[i, i])
            if i != self.n:
                res_str += "*"
        self.lista_krokow.append(res_str)
        res_num = eval(res_str)
        self.lista_krokow.append(res_num)
        self.result = Liczba(res_num)
        self.result_matrix = res_matrix