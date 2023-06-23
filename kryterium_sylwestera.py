from aux import clear_terminal, round_to_n_significant_digits

from operacja_unarna import OperacjaUnarna
from liczba import Liczba
from wyznacznik import Wyznacznik

class KryteriumSylwestera(Wyznacznik):
    nazwa_typu = "KRYT. SYLWESTERA"
    def __init__(self, nazwa, m1):
        Wyznacznik.__init__(self, nazwa, m1)
        
    def enter_m(historia, nazwa = ""):
        clear_terminal()
        print("Podaj macierz")
        m1 = OperacjaUnarna.enter_matrix(historia, 0, 0, True)
        return KryteriumSylwestera(nazwa, m1)
        
    def run_operation(self):
        if not self.m1.is_symmetric():
            self.lista_krokow.append(self.m1.to_str())
            self.lista_krokow.append("Macierz nie jest ani dodatnio, ani ujemnie określona, bo nie jest symetryczna")
            self.result = Liczba(0)
            self.result_matrix = self.m1
        else:
            Wyznacznik.run_operation(self)
            res_matrix = self.get_result_matrix()
            self.lista_krokow = self.get_steps_without_det()
            det_list = []
            for i in range(1, self.n+1):
                color_list1 = [(l, l) for l in range(1, i+1)]
                self.lista_krokow.append(res_matrix.to_str(color_list1))
                res_str = ""
                for j in range(1, i+1):
                    res_str += str(res_matrix[j, j])
                    if j != i:
                        res_str += "*"
                self.lista_krokow.append(res_str)
                res_num = eval(res_str)
                if res_num < 10 ** self.EPSILON_POWER:
                    r_num_round = round_to_n_significant_digits(res_num, self.EPSILON_POWER)
                    diff = res_num - r_num_round
                    if diff < self.EPSILON and diff > -self.EPSILON:
                        res_num = r_num_round
                self.lista_krokow.append(res_num)
                det_list.append(res_num)

            
            flag_pos = False
            flag_neg = False
            flag_zero = False
            if det_list[0] < 0:
                flag_neg = True
            elif det_list[0] > 0:
                flag_pos = True
            else:
                flag_zero = True
                
            for i, e in enumerate(det_list):
                self.lista_krokow.append("det(M" + str(i+1) + ") = " + str(e) + f"{'> 0' if e>0 else ('< 0' if e<0 else '= 0')}")
                if i + 1 % 2 == 1:
                    if flag_pos and e < 0:
                        flag_zero = True
                        break
                    elif flag_pos and e > 0:
                        continue
                    elif flag_neg and e < 0:
                        continue
                    elif flag_neg and e > 0:
                        flag_zero = True
                        break
                    elif e == 0:
                        flag_zero
                        break
                else:
                    if e > 0:
                        continue
                    else:
                        flag_zero = True
                        break
                    
            res_str = "Macierz "   
            if flag_zero:
                res_num = 0
                res_str += "nie jest ani dodatnio, ani ujemnie określona"
            elif flag_pos:
                res_num = 1
                res_str += "jest dodatnio określona"
            elif flag_neg:
                res_num = -1
                res_str += "jest ujemnie określona"
                
                
            self.lista_krokow.append(res_str)
            self.result = Liczba(res_num)
            self.result_matrix = res_matrix
        