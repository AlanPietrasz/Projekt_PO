
from obiekt_matematyczny import ObiektMatematyczny 

class Liczba(ObiektMatematyczny):
    def __init__(self, wartosc):
        self.set_name(str(wartosc))
        self.wartosc = wartosc
        
    def __getitem__(self):
        return self.wartosc
    