
from operacja_unarna import OperacjaUnarna

class OperacjaBinarna(OperacjaUnarna):
    def __init__(self, nazwa, m1, m2):
        OperacjaUnarna.__init__(self, nazwa, m1)
        self.m2 = m2
        self.wymiary2 = m2.get_dimensions()
        