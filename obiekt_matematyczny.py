from aux import clear_terminal, invalid_input

class ObiektMatematyczny:
    zbior_nazw = set()
    def __init__(self, nazwa):
        self.nazwa = nazwa
        
    def type_repr(self):
        return self.nazwa_typu

    def set_name(self, nazwa):
        self.nazwa = nazwa
        
    def __str__(self):
        pass
        
    def __repr__(self):
        return self.nazwa

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