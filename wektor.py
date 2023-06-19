import numpy as np

from aux import clear_terminal
from obiekt_matematyczny import ObiektMatematyczny
from macierz import Macierz

class Wektor(Macierz):
    nazwa_typu = "WEKTOR"
    
    def __init__(self, m, nazwa="", tab=[]):
        super().__init__(m, 1, nazwa, tab)
        
    def create_wektor(nazwa):
        clear_terminal()
        m = Macierz.enter_matrix_size("Podaj liczbę wierszy")
        n = 1
        macierz = Wektor(m, nazwa)
        return Macierz.edit_matrix(macierz, m, n, is_wektor= True)
        

        
