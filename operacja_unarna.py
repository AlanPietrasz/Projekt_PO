
from operacja import Operacja

class OperacjaUnarna(Operacja):
    def __init__(self, nazwa, m1):
        Operacja.__init__(self, nazwa)
        self.m1 = m1
        self.wymiary1 = m1.get_dimensions()