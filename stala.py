from aux import invalid_input

from obiekt_matematyczny import ObiektMatematyczny
from liczba import Liczba

class Stala(Liczba):
    nazwa_typu = "STAŁA"
    
    
    def __init__(self, wartosc, nazwa):
        self.nazwa = nazwa
        self.wartosc = wartosc
        
    def get_value(self):
        return self.wartosc
    
    def __str__(self):
        return str(self.get_value())
    
    def modify(self):
        invalid_input("Nie można modyfikować obiektu Stała")

