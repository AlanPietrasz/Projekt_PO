
from aux import clear_terminal, get_char

from obiekt_matematyczny import ObiektMatematyczny
from macierz import Macierz
from wektor import Wektor
from liczba import Liczba
from stala import Stala
from zmienna import Zmienna
from zbior import Zbior

from historia import Historia

from dodawanie import Dodawanie

class Menu:
    def __init__(self):
        self.historia_obiektow = Historia()
        self.historia_operacji = Historia()
        self.historia_obiektow["id"] = Macierz(3, 3, "id", [[1, 0, 0],
                                                            [0, 1, 0],
                                                            [0, 0, 1]])
        self.historia_obiektow["exm2"] = Macierz(3, 3, "exm2", [[1, 2, 2],
                                                                [0, 1, 0],
                                                                [4, 0, 1]])
        self.historia_obiektow["exm1"] = Macierz(2, 3, "exm1", [[1, 2, 3],
                                                                [0, 1, 2]])
        self.historia_obiektow["exw1"] = Wektor(3, "exw1", [[1, 2, 3]])
        self.historia_obiektow["pi"] = Stala(3.14,"pi")
        self.historia_obiektow["2.5"] = Liczba(2.5)
        self.historia_obiektow["x"] = Zmienna(5, "x")
        zbior1 = Zbior("zbior1")
        # zbior1["id"] = Macierz(3, 3, "id", [[1, 0, 0],
        #                                     [0, 1, 0],
        #                                     [0, 0, 1]])
        zbior1["id4"] = Macierz(4, 4, "id4", [[1, 0, 0, 0],
                                              [0, 1, 0, 0],
                                              [0, 0, 1, 0],
                                              [0, 0, 0, 1]])
        for i in range(10, 20):
            zbior1[str(i)] = Liczba(i)
        self.historia_obiektow["zbior1"] = zbior1
        for i in range(10):
            self.historia_obiektow[str(i)] = Liczba(i)
        

    def display_menu():
        clear_terminal()
        print("------------MENU-GŁÓWNE-----------------")
        print("1. Zarządzanie pamięcią")
        print("2. Dodawanie macierzy")
        print("3. Odejmowanie macierzy")
        print("4. Mnożenie macierzy")
        print("5. Eliminacja Gaussa")
        print("6. Macierz odwrotna")
        print("7. Wyznacznik")
        print("8. Kryterium Sylwestera")
        print("9. Wyjście")
        print("Podaj liczbę:   ", end="")
        # print("1. Dodawanie, odejmowanie i mnożenie macierzy")
        # print("2. Eliminacja Gaussa")
        # print("3. Obliczenie wyznacznika macierzy")
        # print("4. Ortagonalizacja Grama-Schmidta")
        # print("5. Obliczenie Page Ranku")
        # print("6. Sprawdzenie, czy dana macierz jest dodatnio określona przy pomocy kryterium Sylwestera")
        # print("7. Zakończ")

    def display_memory_menu():
        clear_terminal()
        print("------------MENU-PAMIĘCI---------------")
        print("1. Zapisane obiekty matematyczne")
        print("2. Zapisane operacje")
        print("3. Menu Główne")
        print("Podaj liczbę:   ", end="")
    
    def display_object_memory_menu():
        clear_terminal()
        print("------------HISTORIA-OBIEKTÓW---------------")
        print("1. Nowa macierz")
        print("2. Nowy wektor")
        print("3. Nowa liczba")
        print("4. Nowa stała")
        print("5. Nowa zmienna")
        print("6. Nowy zbior")
        print("7. Edytuj wybrany obiekt")
        print("8. Przeglądaj zapisane obiekty matematyczne")
        print("9. Menu Pamięci")
        print("Podaj liczbę:   ", end="")
        
    def display_set_menu():
        clear_terminal()
        print("------------MENU-ZBIORU---------------")
        print("1. Nowa macierz")
        print("2. Nowy wektor")
        print("3. Nowa liczba")
        print("4. Nowa stała")
        print("5. Nowa zmienna")
        print("6. Edytuj wybrany obiekt")
        print("7. Przeglądaj zapisane obiekty matematyczne")
        print("8. Menu historii obiektów")
        print("Podaj liczbę:   ", end="")

    def invalid_input():
        print()
        print("Podano niepoprawne dane")
        user_input = input()
        clear_terminal()
    
    # def create_number_name():
    #     clear_terminal()               
    #     while(True):
    #         print("Podaj wartość")
    #         user_input = input()
    #         if user_input == "":
    #             return ""
    #         if not ObiektMatematyczny.free_name(user_input):
    #             print("Obiekt matematyczny o danej nazwie już istnieje")
    #             user_input = input()
    #             clear_terminal()
    #             continue
    #         return user_input
    
    def create_name():
        clear_terminal()               
        while(True):
            print("Podaj nazwę dla obiektu")
            user_input = input()
            if user_input == "":
                print("Podano nieprawidłową nazwę")
                user_input = input()
                clear_terminal()
                continue
            if not ObiektMatematyczny.is_free_name(user_input):
                print("Obiekt matematyczny o danej nazwie już istnieje")
                user_input = input()
                clear_terminal()
                continue
            return user_input
            
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
                    print("Podano nieprawidłową wartość")
                    user_input = input()
                    clear_terminal()
    
    def enter_matrix_size(message):
        while(True):
            print(message)
            user_input = input()
            if user_input.isdigit():
                s = int(user_input)
                if s < 1 or s > Macierz.MAX_MATRIX_SIZE:
                    print("Podano nieprawidłową wartość")
                    user_input = input()
                    clear_terminal()
                else:
                    return s
            else:
                print("Podano nieprawidłową wartość")
                user_input = input()
                clear_terminal()
    
    def create_matrix(nazwa, is_wektor=False):
        clear_terminal()
        m = Menu.enter_matrix_size("Podaj liczbę wierszy")
        n = 1
        if not is_wektor:
            n = Menu.enter_matrix_size("Podaj liczbę kolumn")
        if is_wektor:
            macierz = Wektor(m, nazwa)
        else:
            macierz = Macierz(m, n, nazwa)
        i = 1
        j = 1
        while True:
            clear_terminal()
            macierz.print(i, j)
            print(f"Używaj wasd, aby poruszać się po {'wektorze' if is_wektor else 'macierzy'}")
            print("Naciśnij ENTER jeśli chcesz wpisać wartość w wybrane pole")
            print(f"Naciśnij q jeśli chcesz zakończyć wypełnianie pól {'wektora' if is_wektor else 'macierzy'}")
            user_input = get_char()
            if user_input == "enter":
                wartosc = Menu.create_number_val()
                macierz[i, j] = wartosc
            elif user_input == "w":
                if i > 1:
                    i -= 1
            elif user_input == "a":
                if j > 1:
                    j -= 1
            elif user_input == "s":
                if i < m:
                    i += 1
            elif user_input == "d":
                if j < n:
                    j += 1
            elif user_input == "q":
                break
            else:
                print("Podano nieprawidłową wartość")
                user_input = input()
        return macierz
    
    def create_set(nazwa):
        zbior = Zbior(nazwa)
        Menu.set_menu(zbior)
        return zbior
    
    def new_matrix(self, kolekcja):
        nazwa = Menu.create_name()
        nowy_obiekt = Menu.create_matrix(nazwa)
        kolekcja[repr(nowy_obiekt)] = nowy_obiekt

    def new_vector(self, kolekcja):
        nazwa = Menu.create_name()
        nowy_obiekt = Menu.create_matrix(nazwa, True)
        kolekcja[repr(nowy_obiekt)] = nowy_obiekt

    def new_number(self, kolekcja):
        while True:
            wartosc = Menu.create_number_val()
            nazwa = str(wartosc)
            if not ObiektMatematyczny.is_free_name(nazwa):
                print("Podana liczba jest już zapisana")
                user_input = input()
                Menu.clear_terminal()
                continue
            break
        nowy_obiekt = Liczba(wartosc)
        kolekcja[repr(nowy_obiekt)] = nowy_obiekt
        
    def new_constant(self, kolekcja):
        nazwa = Menu.create_name()
        wartosc = Menu.create_number_val()
        kolekcja[nazwa] = Stala(wartosc, nazwa)

    def new_variable(self, kolekcja):
        nazwa = Menu.create_name()
        wartosc = Menu.create_number_val()
        kolekcja[nazwa] = Zmienna(wartosc, nazwa)
        
    def new_set(self):
        nazwa = Menu.create_name()
        nowy_obiekt = Menu.create_set(nazwa)
        self.historia_obiektow[nazwa] = nowy_obiekt

    def object_memory_menu(self):
        while (True):
            Menu.display_object_memory_menu()
            user_input = input()
            if (user_input == "1"):
                self.new_matrix(self.historia_obiektow)
            elif (user_input == "2"):
                self.new_vector(self.historia_obiektow)
            elif (user_input == "3"):
                self.new_number(self.historia_obiektow)
            elif (user_input == "4"):
                self.new_constant(self.historia_obiektow)
            elif (user_input == "5"):
                self.new_variable(self.historia_obiektow)
            elif (user_input == "6"):
                self.new_set()
            elif (user_input == "7"):
                pass
            elif (user_input == "8"):
                # self.historia_obiektow.print_all()
                self.historia_obiektow.browse_history()
                # user_input = input()
            elif (user_input == "9"):
                break
            else:
                Menu.invalid_input()

    def set_menu(self, zbior):
        while (True):
            Menu.display_set_menu()
            user_input = input()
            if (user_input == "1"):
                self.new_matrix(zbior)
            elif (user_input == "2"):
                self.new_vector(zbior)
            elif (user_input == "3"):
                self.new_number(zbior)
            elif (user_input == "4"):
                self.new_constant(zbior)
            elif (user_input == "5"):
                self.new_variable(zbior)
            elif (user_input == "6"):
                pass
            elif (user_input == "7"):
                # self.historia_obiektow.print_all()
                zbior.browse_history()
                # user_input = input()
            elif (user_input == "8"):
                break
            else:
                Menu.invalid_input()

    def run(self):
        m1 = self.historia_obiektow.get_val("id")
        m2 = self.historia_obiektow.get_val("exm2")
        d1 = Dodawanie("dod1", m1, m2)
        d1.print_operation_steps()
        
        user_input = input()
        while True:
            Menu.display_menu()
            user_input = input()
            if (user_input == "1"):
                while True:
                    Menu.display_memory_menu()
                    user_input = input()
                    if (user_input == "1"):
                        self.object_memory_menu()
                    elif (user_input == "2"):
                        """
                        TODO
                        """
                        pass
                    elif (user_input == "3"):
                        break
                    else:
                        Menu.invalid_input()
            elif (user_input == "2"):
                
                pass
            elif (user_input == "3"):
                pass
            elif (user_input == "4"):
                pass
            elif (user_input == "5"):
                pass
            elif (user_input == "6"):
                pass
            elif (user_input == "7"):
                pass
            elif (user_input == "8"):
                pass
            elif (user_input == "9"):
                break
            else:
                Menu.invalid_input()


            
            
