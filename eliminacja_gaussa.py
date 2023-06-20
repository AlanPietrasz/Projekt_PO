import copy

from aux import clear_terminal

from macierz import Macierz

from operacja_unarna import OperacjaUnarna

class EliminacjaGaussa(OperacjaUnarna):
    nazwa_typu = "ELIMINACJA G."
    def __init__(self, nazwa, m1):
        OperacjaUnarna.__init__(self, nazwa, m1)
        self.m = self.wymiary1[0]
        self.n = self.wymiary1[1]
        
    def enter_m(historia, nazwa = ""):
        clear_terminal()
        print("Podaj pierwszą macierz")
        m1 = OperacjaUnarna.enter_matrix(historia)
        return EliminacjaGaussa(nazwa, m1)
    
    def run_operation(self):
        res_matrix = self.m1.copy()
        self.lista_krokow.append(res_matrix.to_str())
        zuzyte_wiersze = []
        for kolumna in range(1, self.n+1):
            zbior_niezerowych_wierszy = [i for i 
                                         in range(1, self.m+1) 
                                         if int(res_matrix[i, kolumna]) != 0]
            zbior_niezerowych_wierszy = [x for x in zbior_niezerowych_wierszy if x not in zuzyte_wiersze]
            if zbior_niezerowych_wierszy != []:
                e = min(zbior_niezerowych_wierszy)
                zuzyte_wiersze.append(e)
                color_list1 = [(e, l) for l in range(1, self.n+1)]
                zbior_niezerowych_wierszy.remove(e)
                color_list2 = [(e2, l) for l in range(1, self.n+1) for e2 in zbior_niezerowych_wierszy]
                for wiersz in zbior_niezerowych_wierszy:
                    wspolczynnik = "("+str(res_matrix[wiersz, kolumna])+"/"+str(res_matrix[e, kolumna])+")"
                    for j in range(kolumna, self.n+1):
                        r_str = str(res_matrix[wiersz, j])+\
                            "-("+wspolczynnik+"*"+str(res_matrix[e, j])+")"
                        res_matrix[wiersz, j] = r_str
                        # print(r_str)
                        # input()
                        self.lista_krokow.append(res_matrix.to_str_2_col(color_list1, color_list2))
                        r_num = eval(r_str)
                        if int(r_num) == r_num:
                            res_matrix[wiersz, j] = int(r_num)
                        else:
                            res_matrix[wiersz, j] = r_num
                        self.lista_krokow.append(res_matrix.to_str_2_col(color_list1, color_list2))
                    
        self.result = res_matrix
            
        # for wiersz in range(1, self.m+1):
        #     for i in range(wiersz+1, self.n+1):
        #         if res_matrix[i,wiersz] != 0:
        #             for j in range(wiersz)