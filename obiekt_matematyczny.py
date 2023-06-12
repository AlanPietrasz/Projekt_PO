
class ObiektMatematyczny:
    zbior_nazw = set()
    def __init__(self, nazwa):
        ObiektMatematyczny.set_name(nazwa)
        
    def set_name(self, nazwa):
        if nazwa in self.zbior_nazw:
            raise ValueError("Obiekt matematyczny o danej nazwie już istnieje")
        self.nazwa = nazwa
        self.zbior_nazw.add(nazwa)
        
    def print(self):
        pass
    
    def get_value(self):
        pass
