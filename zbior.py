from obiekt_matematyczny import ObiektMatematyczny

class Zbior(ObiektMatematyczny):
    def __init__(self, nazwa, zbior_wartosci = dict()):
        ObiektMatematyczny.set_name(nazwa)
        self.zbior_wartosci = zbior_wartosci
        
    # def __setitem__(self, obiekt)
        
    # def __getitem__(self, nazwa)