
from liczba import Liczba

class Zmienna(Liczba):
    slownik_wartosci = dict()
    
    def __init__(self, wartosc, nazwa):
        self.set_name(nazwa)
        self.slownik_wartosci[self.nazwa] = wartosc
        
    def get_value(self):
        return self.slownik_wartosci[self.nazwa]
    
    def get_name(self):
        return super().get_name()
    
    def change_value(self, wartosc):
        self.slownik_wartosci[self.nazwa] = wartosc
        