from aux import clear_terminal, get_char
from collections import defaultdict as dd
from colorama import Fore, Style

from obiekt_matematyczny import ObiektMatematyczny
from macierz import Macierz
from wektor import Wektor
from liczba import Liczba
from stala import Stala
from zmienna import Zmienna

class Zbior(ObiektMatematyczny):
    MAX_NUMBER_OF_SHOWED_ELEMS = 10
    MAX_SET_LEN = 20
    zbior_nazw = list()
    
    def __init__(self, nazwa, zbior_wartosci = dd()):
        self.set_name(nazwa)
        self.zbior_wartosci = zbior_wartosci
        
    def __setitem__(self, nazwa, obiekt):
        if self.set_len() >= Zbior.MAX_SET_LEN:
            raise ValueError("Osiągnięto maksymalną liczbę obiektów matematycznych w danym zbiorze")
        else:
            if not Zbior.is_free_name(nazwa):
                raise ValueError("Obiekt matematyczny o danej nazwie już istnieje w zbiorze")
            self.zbior_wartosci[nazwa] = obiekt
            Zbior.zbior_nazw.append(nazwa)
        
    def __getitem__(self, nazwa):
        return self.zbior_wartosci[nazwa]
    
    def is_free_name(nazwa):
        if nazwa in Zbior.zbior_nazw:
            return False
        return True
    
    def set_len(self):
        return len(self.zbior_nazw)

    def remove(self, nazwa):
        Zbior.zbior_nazw.remove(nazwa)
        self.zbior_wartosci.pop(nazwa)
        
    def print_type_repr(obiekt):
        if isinstance(obiekt, Zmienna):
            return "Zmienna "
        elif isinstance(obiekt, Stala):
            return "Stała   "
        elif isinstance(obiekt, Liczba):
            return "Liczba  "
        elif isinstance(obiekt, Zbior):
            return "Zbiór   "       
        elif isinstance(obiekt, Wektor):
            return "Wektor  "  
        elif isinstance(obiekt, Macierz):
            return "Macierz " 
        
    def show_object(self, i):
        object = self.zbior_wartosci[self.zbior_nazw[i-1]]
        if not isinstance(object, Liczba) or isinstance(object, Stala) or isinstance(object, Zmienna):
            print(repr(object))
        print(object)
        user_input = input() 
        
    def print_range(self, b, e, chosen=0, color=Fore.GREEN):
        if b - e > Zbior.MAX_NUMBER_OF_SHOWED_ELEMS:
            e = b + Zbior.MAX_NUMBER_OF_SHOWED_ELEMS
        if e > self.set_len():
            e = self.set_len()
        clear_terminal()
        print("---------ZBIÓR-----------")
        print("Nazwa zbioru: ", self.nazwa)
        max_len = len(str(e))
        for i in range(b-1, e):
            obiekt = self.zbior_wartosci[self.zbior_nazw[i]]
            print(f"{Fore.YELLOW}{i+1}: {Style.RESET_ALL}", end="")
            print(" " * (max_len - len(str(i+1))), end="")
            print(f"{Fore.CYAN}{Zbior.print_type_repr(obiekt)} {Style.RESET_ALL}", end="")
            if i != chosen - 1: 
                print(repr(obiekt))
            else:
                print(f"{color}{repr(obiekt)}{Style.RESET_ALL}")


    def browse_set(self):
        i = 1
        chosen = 1
        while True:
            self.print_range(i, i + self.MAX_NUMBER_OF_SHOWED_ELEMS, chosen)
            print("Używaj ws, aby poruszać się po zbiorze")
            print("Naciśnij ENTER jeśli chcesz zobaczyć wartość w wybranym polu")
            print("Naciśnij q jeśli chcesz zakończyć przeglądanie zbioru")
            user_input = get_char()
            if user_input == "enter":
                self.show_object(chosen)
            elif user_input == "w":
                if chosen - 1 < i:
                    if i > 1:
                        i -= 1
                        chosen -= 1
                else:
                    chosen -= 1

            elif user_input == "s":
                if chosen + 1 > i + self.MAX_NUMBER_OF_SHOWED_ELEMS:
                    if i + self.MAX_NUMBER_OF_SHOWED_ELEMS < self.set_len():
                        i += 1
                        chosen += 1
                else:
                    chosen += 1
            elif user_input == "q":
                break
            else:
                print("Podano nieprawidłową wartość")
                user_input = input()
        
    # def __setitem__(self, obiekt)
        
    # def __getitem__(self, nazwa)