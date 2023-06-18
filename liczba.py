
from aux import clear_terminal
from obiekt_matematyczny import ObiektMatematyczny 


class Liczba(ObiektMatematyczny):
    def __init__(self, wartosc):
        self.set_name(str(wartosc))
        self.wartosc = wartosc
        
    def get_value(self):
        return self.wartosc
    
    def __str__(self):
        return str(self.get_value())
    
