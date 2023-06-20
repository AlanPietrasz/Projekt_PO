import numpy as np
from colorama import Fore, Style

from operacja_unarna import OperacjaUnarna

class OperacjaBinarna(OperacjaUnarna):
    def __init__(self, nazwa, m1, m2):
        OperacjaUnarna.__init__(self, nazwa, m1)
        self.m2 = m2
        self.wymiary2 = m2.get_dimensions()
        
    def str_m_op_m(self, other, operator="o", color_list1=[], color_list2=[], color=Fore.GREEN, color2=Fore.CYAN):
        res = ""
        arr = self.macierz
        arr2 = other.macierz
        max_width = np.vectorize(lambda x: len(str(x)))(arr).max()
        max_width2 = np.vectorize(lambda x: len(str(x)))(arr2).max()
        n_len = len(str(self.n))
        m_len = len(str(self.m))
        n2_len = len(str(other.n))
        m2_len = len(str(other.m))
        res += " " * (2 + n_len)
        for j in range(arr.shape[1]):
            res += " " * (max_width - len(str(j)))
            res += f"{color2}{j+1}:{Style.RESET_ALL}"
        res += " " * 3
        res += " " * (2 + n2_len)
        for j in range(arr2.shape[1]):
            res += " " * (max_width2 - len(str(j)))
            res += f"{color2}{j+1}:{Style.RESET_ALL}"
        res += "\n"
        
        for i in range(arr.shape[0]):
            res += f"{color2}{i+1}:{Style.RESET_ALL} "
            res += " " * (m_len - (len(str(i+1))))
            for j in range(arr.shape[1]):
                if (i + 1, j + 1) in color_list1:
                    res += f"{color}{str(arr[i, j]).rjust(max_width)}{Style.RESET_ALL} "
                else:
                    res += str(arr[i, j]).rjust(max_width) + " "
            
            res += f" {operator if i == int(self.m / 2) else ' '} "
            
            res += f"{color2}{i+1}:{Style.RESET_ALL} "
            res += " " * (m2_len - (len(str(i+1))))
            for j in range(arr2.shape[1]):
                if (i + 1, j + 1) in color_list2:
                    res += f"{color}{str(arr2[i, j]).rjust(max_width2)}{Style.RESET_ALL} "
                else:
                    res += str(arr2[i, j]).rjust(max_width2) + " "
                    
            res += "\n"
        return res
    
    def str_m_op_m_eq_m(self, other, other2, operator="o", color_list1=[], color_list2=[], color_list3=[], color=Fore.GREEN, color2=Fore.CYAN):
        res = ""
        arr = self.macierz
        arr2 = other.macierz
        arr3 = other2.macierz
        height = max([arr.shape[0], arr2.shape[0], arr3.shape[0]])
        max_width = np.vectorize(lambda x: len(str(x)))(arr).max()
        max_width2 = np.vectorize(lambda x: len(str(x)))(arr2).max()
        max_width3 = np.vectorize(lambda x: len(str(x)))(arr3).max()
        n_len = len(str(self.n))
        m_len = len(str(self.m))
        n2_len = len(str(other.n))
        m2_len = len(str(other.m))
        n3_len = len(str(other2.n))
        m3_len = len(str(other2.m))
        res += " " * (2 + n_len)
        for j in range(arr.shape[1]):
            res += " " * (max_width - len(str(j)))
            res += f"{color2}{j+1}:{Style.RESET_ALL}"
        res += " " * 3
        res += " " * (2 + n2_len)
        for j in range(arr2.shape[1]):
            res += " " * (max_width2 - len(str(j)))
            res += f"{color2}{j+1}:{Style.RESET_ALL}"
        res += " " * 3
        res += " " * (2 + n3_len)
        for j in range(arr3.shape[1]):
            res += " " * (max_width3 - len(str(j)))
            res += f"{color2}{j+1}:{Style.RESET_ALL}"
        res += "\n"
        
        for i in range(height):
            if not arr.shape[0] < i + 1:
                res += f"{color2}{i+1}:{Style.RESET_ALL} "
                res += " " * (m_len - (len(str(i+1))))
                for j in range(arr.shape[1]):
                    if (i + 1, j + 1) in color_list1:
                        res += f"{color}{str(arr[i, j]).rjust(max_width)}{Style.RESET_ALL} "
                    else:
                        res += str(arr[i, j]).rjust(max_width) + " "
            else:
                res += " " * (m_len + 1) + " " * ((max_width + 1) * arr.shape[1]) + " " 
            
            res += f" {operator if i == int(self.m / 2) else ' '} "
            
            if not arr2.shape[0] < i + 1:
                res += f"{color2}{i+1}:{Style.RESET_ALL} "
                res += " " * (m2_len - (len(str(i+1))))
                for j in range(arr2.shape[1]):
                    if (i + 1, j + 1) in color_list2:
                        res += f"{color}{str(arr2[i, j]).rjust(max_width2)}{Style.RESET_ALL} "
                    else:
                        res += str(arr2[i, j]).rjust(max_width2) + " "

            else:
                res += " " * m2_len + " " * max_width2 + " " 
 
            res += f" {'=' if i == int(self.m / 2) else ' '} "
            
            if not arr.shape[0] < i + 1:
                res += f"{color2}{i+1}:{Style.RESET_ALL} "
                res += " " * (m3_len - (len(str(i+1))))
                for j in range(arr3.shape[1]):
                    if (i + 1, j + 1) in color_list3:
                        res += f"{color}{str(arr3[i, j]).rjust(max_width3)}{Style.RESET_ALL} "
                    else:
                        res += str(arr3[i, j]).rjust(max_width3) + " "
            else:
                res += " " * m3_len + " " * max_width3 + " " 
            
                    
            res += "\n"
        return res
    
       
    def str_num_op_m_eq_m(self, other, other2, operator="o", color_list1=[], color_list2=[], color_list3=[], color=Fore.GREEN, color2=Fore.CYAN):
        res = ""
        num = self.get_value()
        arr = other.macierz
        arr2 = other2.macierz
        height = max([arr.shape[0], arr2.shape[0]])
        num_width = len(str(num))
        max_width = np.vectorize(lambda x: len(str(x)))(arr).max()
        max_width2 = np.vectorize(lambda x: len(str(x)))(arr2).max()
        n_len = len(str(other.n))
        m_len = len(str(other.m))
        n2_len = len(str(other2.n))
        m2_len = len(str(other2.m))
        
        res += " "*(num_width+2)
        res += " " * 3
        res += " " * (2 + n_len)
        for j in range(arr.shape[1]):
            res += " " * (max_width - len(str(j)))
            res += f"{color2}{j+1}:{Style.RESET_ALL}"
        res += " " * 3
        res += " " * (2 + n2_len)
        for j in range(arr2.shape[1]):
            res += " " * (max_width2 - len(str(j)))
            res += f"{color2}{j+1}:{Style.RESET_ALL}"
        res += "\n"
        
        for i in range(height):
            
            res += f" {str(num) if i == int(other.m / 2) else ' '*num_width} "
            
            res += f" {operator if i == int(other.m / 2) else ' '} "
            
            if not arr.shape[0] < i + 1:
                res += f"{color2}{i+1}:{Style.RESET_ALL} "
                res += " " * (m_len - (len(str(i+1))))
                for j in range(arr.shape[1]):
                    if (i + 1, j + 1) in color_list2:
                        res += f"{color}{str(arr[i, j]).rjust(max_width)}{Style.RESET_ALL} "
                    else:
                        res += str(arr[i, j]).rjust(max_width) + " "

            else:
                res += " " * m_len + " " * max_width + " " 
 
            res += f" {'=' if i == int(other.m / 2) else ' '} "
            
            if not arr2.shape[0] < i + 1:
                res += f"{color2}{i+1}:{Style.RESET_ALL} "
                res += " " * (m2_len - (len(str(i+1))))
                for j in range(arr2.shape[1]):
                    if (i + 1, j + 1) in color_list3:
                        res += f"{color}{str(arr2[i, j]).rjust(max_width2)}{Style.RESET_ALL} "
                    else:
                        res += str(arr2[i, j]).rjust(max_width2) + " "
            else:
                res += " " * m2_len + " " * max_width2 + " " 
            
                    
            res += "\n"
        return res