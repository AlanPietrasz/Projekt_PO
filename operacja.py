import numpy as np

my_list = [["abc", "def", "ghi"],
           ["jkl", "mno", "pqr"],
           ["stu", "vwx", "yz"]]

my_array = np.array(my_list, dtype=np.str_)

print(my_array)



class Operacja:
    def __init__(self, nazwa):
        self.nazwa = nazwa