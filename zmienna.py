
from obiekt_matematyczny import ObiektMatematyczny
from liczba import Liczba

class Zmienna(Liczba):
    nazwa_typu = "ZMIENNA"
    
    def __init__(self, wartosc, nazwa):
        self.nazwa = nazwa
        self.wartosc = wartosc
      
    def get_value(self):
        return self.wartosc
    
    def set_value(self, wartosc):
        self.wartosc = wartosc
        
    def __str__(self):
        return str(self.get_value())
    
    def modify(self):
        self.set_value(ObiektMatematyczny.create_number_val())
    
