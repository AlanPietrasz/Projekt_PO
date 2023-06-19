from aux import clear_terminal, invalid_input

class ObiektMatematyczny:
    zbior_nazw = set()
    def __init__(self, nazwa):
        self.nazwa = nazwa
        
    def type_repr(self):
        return self.nazwa_typu

    def set_name(self, nazwa):
        self.nazwa = nazwa
        
    # def set_name(self, nazwa):
    #     if self.free_name(nazwa):
    #         raise ValueError("Obiekt matematyczny o danej nazwie już istnieje")
    #     self.nazwa = nazwa
    #     self.zbior_nazw.add(nazwa)
        
    # def free_name(self, nazwa):
    #     if nazwa in self.zbior_nazw:
    #         return False
    #     return True
        
    # def set_name(self, nazwa):
    #     if not ObiektMatematyczny.is_free_name(nazwa):
    #         raise ValueError("Obiekt matematyczny o danej nazwie już istnieje")
    #     self.nazwa = nazwa
    #     if nazwa != "":
    #         ObiektMatematyczny.zbior_nazw.add(nazwa)
        
    # def is_free_name(nazwa):
    #     if nazwa in ObiektMatematyczny.zbior_nazw:
    #         return False
    #     return True
        
    def __str__(self):
        pass
        #return self.nazwa
        
    def __repr__(self):
        return self.nazwa
    # def print(self):
    #     pass
    
    def get_value(self):
        pass
    
    def print_all():
        for e in ObiektMatematyczny.zbior_nazw:
            print(e)

    def create_number_val():
        clear_terminal()               
        while(True):
            print("Podaj wartość")
            user_input = input()
            try:
                user_input = int(user_input)
                return int(user_input)
            except:
                try:
                    user_input = float(user_input)
                    return float(user_input)
                except:
                    invalid_input("Podano nieprawidłową wartość")