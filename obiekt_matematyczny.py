
class ObiektMatematyczny:
    zbior_nazw = set()
    def __init__(self, nazwa):
        ObiektMatematyczny.set_name(nazwa)
        
    # def set_name(self, nazwa):
    #     if self.free_name(nazwa):
    #         raise ValueError("Obiekt matematyczny o danej nazwie już istnieje")
    #     self.nazwa = nazwa
    #     self.zbior_nazw.add(nazwa)
        
    # def free_name(self, nazwa):
    #     if nazwa in self.zbior_nazw:
    #         return False
    #     return True
        
    def set_name(self, nazwa):
        if not ObiektMatematyczny.is_free_name(nazwa):
            raise ValueError("Obiekt matematyczny o danej nazwie już istnieje")
        self.nazwa = nazwa
        ObiektMatematyczny.zbior_nazw.add(nazwa)
        
    def is_free_name(nazwa):
        if nazwa in ObiektMatematyczny.zbior_nazw:
            return False
        return True
        
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
    
    
