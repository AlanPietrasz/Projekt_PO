import numpy as np

from macierz import Macierz

class Wektor(Macierz):
    def __init__(self, m, nazwa="", tab=[]):
        super().__init__(m, 1, nazwa, tab)