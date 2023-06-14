import os

from obiekt_matematyczny import ObiektMatematyczny
from macierz import Macierz
from wektor import Wektor
from liczba import Liczba
from stala import Stala
from zmienna import Zmienna
from zbior import Zbior

# from historia_obiektow import HistoriaObiektow
# from historia_operacji import HistoriaOperacji
from historia import Historia

class Menu:
    def __init__(self):
        self.historia_obiektow = Historia()
        self.historia_operacji = Historia()

    def display_menu():
        Menu.clear_terminal()
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
        Menu.clear_terminal()
        print("------------MENU-PAMIĘCI---------------")
        print("1. Zapisane obiekty matematyczne")
        print("2. Zapisane operacje")
        print("3. Menu Główne")
        print("Podaj liczbę:   ", end="")
    
    def display_object_memory_menu():
        Menu.clear_terminal()
        print("------------HISTORIA-OBIEKTÓW---------------")
        print("1. Nowa macierz")
        print("2. Nowy wektor")
        print("3. Nowa liczba")
        print("4. Nowa stała")
        print("5. Nowa zmienna")
        print("6. Nowy zbior")
        print("7. Usuń wybrane obiekty")
        print("8. Edytuj wybrany obiekt")
        print("9. Przeglądaj zapisane obiekty matematyczne")
        print("10. Menu Pamięci")
        print("Podaj liczbę:   ", end="")
        
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    def invalid_input():
        print()
        print("Podano niepoprawne dane")
        user_input = input()
        Menu.clear_terminal()
    
    def create_name():
        Menu.clear_terminal()               
        while(True):
            print("Podaj nazwę dla obiektu lub naciśnij ENTER jeśli nie chcesz go nazywać")
            user_input = input()
            if user_input == "":
                return ""
            if not ObiektMatematyczny.free_name(user_input):
                print("Obiekt matematyczny o danej nazwie już istnieje")
                user_input = input()
                Menu.clear_terminal()
                continue
            return user_input
            
    def create_number_val():
        Menu.clear_terminal()               
        while(True):
            print("Podaj wartość")
            user_input = input()
            if user_input == "":
                return ""
            if user_input.isdigit():
                return int(user_input)
            try:
                user_input = float(user_input)
                return float(user_input)
            except:
                print("Podano nieprawidłową wartość")
                user_input = input()
                Menu.clear_terminal()
            

    def run(self):
        ObiektMatematyczny.print_all()
        l1 = Liczba(5000)
        print(l1)
        print(repr(l1))
        print(str(l1))
        user_input = input()

        while (True):
            Menu.display_menu()
            user_input = input()
            if (user_input == "1"):
                while (True):
                    Menu.display_memory_menu()
                    user_input = input()
                    if (user_input == "1"):
                        while (True):
                            Menu.display_object_memory_menu()
                            user_input = input()
                            if (user_input == "1"):
                                nazwa = Menu.create_name()
                                
                                pass
                            elif (user_input == "2"):
                                pass
                            elif (user_input == "3"):
                                
                                while True:
                                    wartosc = Menu.create_number_val()
                                    nazwa = str(wartosc)
                                    if not ObiektMatematyczny.free_name(nazwa):
                                        print("Podana liczba jest już zapisana")
                                        user_input = input()
                                        Menu.clear_terminal()
                                        continue
                                    break
                                nowy_obiekt = Liczba(wartosc)
                                self.historia_obiektow[repr(nowy_obiekt)] = nowy_obiekt
                                pass
                            elif (user_input == "4"):
                                nazwa = Menu.create_name()
                                wartosc = Menu.create_number_val()
                                self.historia_obiektow[nazwa] = Liczba()
                                pass
                            elif (user_input == "5"):
                                nazwa = Menu.create_name()
                                wartosc = Menu.create_number_val()
                                self.historia_obiektow[nazwa] = Liczba()
                                pass
                            
                            elif (user_input == "6"):
                                pass
                            elif (user_input == "7"):
                                pass
                            elif (user_input == "8"):
                                pass
                            elif (user_input == "9"):
                                self.historia_obiektow.print_all()
                                user_input = input()
                            elif (user_input == "10"):
                                break
                            else:
                                Menu.invalid_input()
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


            
            
