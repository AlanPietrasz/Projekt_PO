

from obiekt_matematyczny import ObiektMatematyczny
from liczba import Liczba

class Stala(Liczba):
    nazwa_typu = "STAŁA"
    slownik_wartosci = dict()
    
    
    def __init__(self, wartosc, nazwa):
        self.nazwa = nazwa
        self.slownik_wartosci[self.nazwa] = wartosc
        
    def get_value(self):
        return self.slownik_wartosci[self.nazwa]
    
    def __str__(self):
        return str(self.get_value())

