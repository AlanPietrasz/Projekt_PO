from aux import clear_terminal, round_to_n_significant_digits

from operacja_unarna import OperacjaUnarna

class EliminacjaGaussa(OperacjaUnarna):
    EPSILON_POWER = 9
    EPSILON = 10 ** -EPSILON_POWER
    nazwa_typu = "ELIMINACJA G."
    def __init__(self, nazwa, m1):
        OperacjaUnarna.__init__(self, nazwa, m1)
        self.m = self.wymiary1[0]
        self.n = self.wymiary1[1]
    
    def enter_m(historia, nazwa = ""):
        clear_terminal()
        print("Podaj macierz")
        m1 = OperacjaUnarna.enter_matrix(historia)
        return EliminacjaGaussa(nazwa, m1)
    
    def run_operation(self):
        res_matrix = self.m1.copy()
        self.lista_krokow.append(res_matrix.to_str())
        zuzyte_wiersze = []
        for kolumna in range(1, self.n+1):
            zbior_niezerowych_wierszy = [i for i 
                                         in range(1, self.m+1) 
                                         if float(res_matrix[i, kolumna]) != 0.0]            
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
                        self.lista_krokow.append(res_matrix.to_str_2_col(color_list1, color_list2))
                        r_num = eval(r_str)
                        if r_num < 10 ** self.EPSILON_POWER:
                            r_num_round = round_to_n_significant_digits(r_num, self.EPSILON_POWER)
                            diff = r_num - r_num_round
                            if diff < self.EPSILON and diff > -self.EPSILON:
                                r_num = r_num_round
                        if int(r_num) == r_num:
                            res_matrix[wiersz, j] = int(r_num)
                        else:
                            res_matrix[wiersz, j] = r_num
                        self.lista_krokow.append(res_matrix.to_str_2_col(color_list1, color_list2))
        
        self.licznik_zamiany_kolumn = 0
        ustawione = 0
        for kolumna in range(1, self.n+1):
            if ustawione == self.m:
                break
            zerowe_wiersze = []
            niezerowe_wiersze = []
            
            for wiersz in range(ustawione+1, self.m+1):
                if float(res_matrix[wiersz, kolumna]) == 0:
                    zerowe_wiersze.append(wiersz)
                else:
                    niezerowe_wiersze.append(wiersz)
                    
            do_ustawienia = ustawione + len(niezerowe_wiersze)
                        
            for zerowy_wiersz in zerowe_wiersze:
                if zerowy_wiersz <= do_ustawienia:
                    color_list1 = [(zerowy_wiersz, l) for l in range(1, self.n+1)]
                    if niezerowe_wiersze != []:
                        wiersz_do_przestawienia = max(niezerowe_wiersze)
                        niezerowe_wiersze.remove(wiersz_do_przestawienia)
                        color_list2 = [(wiersz_do_przestawienia, l) for l in range(1, self.n+1)]
                        self.lista_krokow.append(res_matrix.to_str_2_col(color_list1, color_list2))
                        res_matrix.swap_rows(zerowy_wiersz, wiersz_do_przestawienia)
                        self.licznik_zamiany_kolumn += 1
                        self.lista_krokow.append(res_matrix.to_str_2_col(color_list2, color_list1))
                        
            ustawione = do_ustawienia
                    
        self.result = res_matrix
        