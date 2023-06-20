
from aux import clear_terminal, invalid_input
from obiekt_matematyczny import ObiektMatematyczny 


class Liczba(ObiektMatematyczny):
    nazwa_typu = "LICZBA"
    
    def __init__(self, wartosc):
        self.nazwa = str(wartosc)
        self.wartosc = wartosc
        
    def get_value(self):
        return self.wartosc
    
    def __str__(self):
        return str(self.get_value())
    
    def modify(self):
        invalid_input("Nie można modyfikować obiektu Liczba")
    
