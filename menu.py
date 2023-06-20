
from aux import clear_terminal, invalid_input

from obiekt_matematyczny import ObiektMatematyczny
from macierz import Macierz
from wektor import Wektor
from liczba import Liczba
from stala import Stala
from zmienna import Zmienna
from zbior import Zbior

from historia import Historia
from historia_obiektow import HistoriaObiektow
from historia_operacji import HistoriaOperacji

from dodawanie import Dodawanie
from odejmowanie import Odejmowanie
from mnozenie import Mnozenie
from eliminacja_gaussa import EliminacjaGaussa

class Menu:
    def __init__(self):
        self.historia_obiektow = HistoriaObiektow()
        self.historia_operacji = HistoriaOperacji()
        self.historia_obiektow["id"] = Macierz(3, 3, "id", [[1, 0, 0],
                                                            [0, 1, 0],
                                                            [0, 0, 1]])
        self.historia_obiektow["exm2"] = Macierz(3, 3, "exm2", [[1, 2, 2],
                                                                [0, 1, 0],
                                                                [4, 0, 1]])
        self.historia_obiektow["exm1"] = Macierz(2, 3, "exm1", [[1, 2, 3],
                                                                [0, 1, 2]])
        self.historia_obiektow["exm3"] = Macierz(3, 5, "exm3", [[1, 2, 3, 4, 6],
                                                                [1, 2, 3, 8, 7],
                                                                [0, 1, 2, 3, 2]])
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
            
        self.historia_operacji["dod1"] = Dodawanie("dod1",
                                                   self.historia_obiektow["id"],
                                                   self.historia_obiektow["exm2"])
        self.historia_operacji["od1"] = Odejmowanie("od1",
                                                    self.historia_obiektow["id"],
                                                    self.historia_obiektow["exm2"])
        self.historia_operacji["mn1"] = Mnozenie("mn1",
                                                 self.historia_obiektow["id"],
                                                 self.historia_obiektow["exm2"])
        self.historia_operacji["mn2"] = Mnozenie("mn2",
                                                 self.historia_obiektow["exm1"],
                                                 self.historia_obiektow["exm3"])
        self.historia_operacji["eg1"] = EliminacjaGaussa("eg1",
                                                        self.historia_obiektow["id"])
        self.historia_operacji["eg2"] = EliminacjaGaussa("eg2",
                                                        self.historia_obiektow["exm3"])
        self.historia_operacji["eg3"] = EliminacjaGaussa("eg3",
                                                        self.historia_obiektow["exm2"])
        self.historia_operacji["eg4"] = EliminacjaGaussa("eg4",
                                                        self.historia_obiektow["exm1"])

    def display_menu():
        clear_terminal()
        print("------------MENU-GŁÓWNE-----------------")
        print("1. Zarządzanie pamięcią")
        print("2. Dodawanie macierzy")
        print("3. Odejmowanie macierzy")
        print("4. Mnożenie macierzy przez skalar")
        print("5. Mnożenie macierzy")
        print("6. Eliminacja Gaussa")
        print("7. Macierz odwrotna")
        print("8. Wyznacznik")
        print("9. Kryterium Sylwestera")
        print("10. Wyjście")
        print("Podaj liczbę:   ", end="")
        # print("1. Dodawanie, odejmowanie i mnożenie macierzy")
        # print("2. Eliminacja Gaussa")
        # print("3. Obliczenie wyznacznika macierzy")
        # print("4. Ortagonalizacja Grama-Schmidta")
        # print("5. Obliczenie Page Ranku")
        # print("6. Sprawdzenie, czy dana macierz jest dodatnio określona przy pomocy kryterium Sylwestera")
        # print("7. Zakończ")


    def run(self):
        # m1 = self.historia_obiektow.get_val("id")
        # m2 = self.historia_obiektow.get_val("exm2")
        # d1 = Dodawanie("dod1", m1, m2)
        # d1.print_operation_steps()
        
        # user_input = input()
        while True:
            Menu.display_menu()
            user_input = input()
            if (user_input == "1"):
                while True:
                    Historia.display_memory_menu()
                    user_input = input()
                    if (user_input == "1"):
                        self.historia_obiektow.object_memory_menu()
                    elif (user_input == "2"):
                        self.historia_operacji.operation_memory_menu()
                    elif (user_input == "3"):
                        break
                    else:
                        invalid_input("Podano niepoprawne dane")
            elif (user_input == "2"):
                operacja = Dodawanie.enter_m_m(self.historia_obiektow)
                operacja.print_and_save(self)
            elif (user_input == "3"):
                operacja = Odejmowanie.enter_m_m(self.historia_obiektow)
                operacja.print_and_save(self)
            elif (user_input == "4"):
                pass
            elif (user_input == "5"):
                operacja = Mnozenie.enter_m_m(self.historia_obiektow)
                operacja.print_and_save(self)
            elif (user_input == "6"):
                operacja = EliminacjaGaussa.enter_m(self.historia_obiektow)
                operacja.print_and_save(self)
            elif (user_input == "7"):
                pass
            elif (user_input == "8"):
                pass
            elif (user_input == "9"):
                pass
            elif (user_input == "10"):
                break
            else:
                invalid_input("Podano niepoprawne dane")


            
            
