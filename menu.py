
from aux import clear_terminal, invalid_input

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
from mnozenie_przez_skalar import MnozeniePrzezSkalar
from wyznacznik import Wyznacznik
from kryterium_sylwestera import KryteriumSylwestera

class Menu:
    def __init__(self):
        self.historia_obiektow = HistoriaObiektow()
        self.historia_operacji = HistoriaOperacji()
        self.historia_obiektow["macierz_id3"] = Macierz(3, 3, "macierz_id3", [[1, 0, 0],
                                                                              [0, 1, 0],
                                                                              [0, 0, 1]])
        self.historia_obiektow["macierz1"] = Macierz(3, 3, "macierz1", [[1, 2, 2],
                                                                        [0, 1, 0],
                                                                        [4, 0, 1]])
        self.historia_obiektow["macierz2"] = Macierz(2, 3, "macierz2", [[1, 2, 3],
                                                                        [0, 1, 2]])
        self.historia_obiektow["macierz3"] = Macierz(3, 5, "macierz3", [[1, 2, 3, 4, 6],
                                                                        [1, 2, 3, 8, 7],
                                                                        [0, 1, 2, 3, 2]])
        self.historia_obiektow["macierz4"] = Macierz(3, 5, "macierz4", [[0, 2, 3, 4, 6],
                                                                        [0, 0, 3, 8, 7],
                                                                        [3, 1, 2, 3, 2]])
        self.historia_obiektow["macierz5"] = Macierz(3, 3, "macierz5", [[5, 2, -1],
                                                                        [0, 0, 1],
                                                                        [6, 2, 3]])
        self.historia_obiektow["macierz6"] = Macierz(3, 3, "macierz6", [[5, 5, 5],
                                                                        [2, 1, -1],
                                                                        [3, 4, 6]])
        self.historia_obiektow["macierz7"] = Macierz(3, 3, "macierz7", [[1, 2, 0],
                                                                        [-1, 2, 0],
                                                                        [0, 0, 1]])
        self.historia_obiektow["macierz8"] = Macierz(3, 3, "macierz8", [[2, 2, 0],
                                                                        [2, 2, 0],
                                                                        [0, 0, 1]])
        self.historia_obiektow["macierz9"] = Macierz(3, 3, "macierz9", [[6, 2, 4],
                                                                        [2, 1, 1],
                                                                        [4, 1, 5]])
        self.historia_obiektow["macierz10"] = Macierz(5, 7, "macierz10", [[1, 4, 3, 7, 3, 6, 4],
                                                                          [5, 2, 8, 2, 7, 3, 1],
                                                                          [3, 7, 0, 1, 5, 9, 1],
                                                                          [1, 5, 3, 9, 2, 9, 0],
                                                                          [1, 5, 2, 3, 8, 7, 2]])
        self.historia_obiektow["wektor1"] = Wektor(3, "wektor1", [[1, 2, 3]])
        self.historia_obiektow["pi"] = Stala(3.14,"pi")
        self.historia_obiektow["2.5"] = Liczba(2.5)
        self.historia_obiektow["x"] = Zmienna(5, "x")
        zbior1 = Zbior("zbior_macierzy_id")
        zbior1["macierz_id2"] = Macierz(2, 2, "macierz_id2", [[1, 0],
                                                              [0, 1]])     
        zbior1["macierz_id3"] = Macierz(3, 3, "macierz_id3", [[1, 0, 0],
                                                              [0, 1, 0],
                                                              [0, 0, 1]])
        zbior1["macierz_id4"] = Macierz(4, 4, "macierz_id4", [[1, 0, 0, 0],
                                                              [0, 1, 0, 0],
                                                              [0, 0, 1, 0],
                                                              [0, 0, 0, 1]])
        for i in range(10):
            zbior1[str(i)] = Liczba(i)
        self.historia_obiektow["zbior1"] = zbior1
        for i in range(10):
            self.historia_obiektow[str(i)] = Liczba(i)
            
        self.historia_operacji["dodawanie1"] = Dodawanie("dodawanie1",
                                                        self.historia_obiektow["macierz_id3"],
                                                        self.historia_obiektow["macierz1"])
        self.historia_operacji["odejmowanie1"] = Odejmowanie("odejmowanie1",
                                                            self.historia_obiektow["macierz_id3"],
                                                            self.historia_obiektow["macierz1"])
        self.historia_operacji["mnozenie1"] = Mnozenie("mnozenie1",
                                                        self.historia_obiektow["macierz_id3"],
                                                        self.historia_obiektow["macierz1"])
        self.historia_operacji["mnozenie2"] = Mnozenie("mnozenie2",
                                                        self.historia_obiektow["macierz2"],
                                                        self.historia_obiektow["macierz3"])
        self.historia_operacji["mnozenie_sk1"] = MnozeniePrzezSkalar("mnozenie_sk1",
                                                                    self.historia_obiektow["x"],
                                                                    self.historia_obiektow["macierz4"])
        self.historia_operacji["elim_g1"] = EliminacjaGaussa("elim_g1",
                                                            self.historia_obiektow["macierz3"])
        self.historia_operacji["elim_g2"] = EliminacjaGaussa("elim_g2",
                                                            self.historia_obiektow["macierz4"])
        self.historia_operacji["elim_g3"] = EliminacjaGaussa("elim_g3",
                                                            self.historia_obiektow["macierz5"])
        self.historia_operacji["wyznacznik1"] = Wyznacznik("wyznacznik1",
                                                            self.historia_obiektow["macierz_id3"])
        self.historia_operacji["wyznacznik2"] = Wyznacznik("wyznacznik2",
                                                            self.historia_obiektow["macierz5"])
        self.historia_operacji["wyznacznik3"] = Wyznacznik("wyznacznik3",
                                                            self.historia_obiektow["macierz6"])
        self.historia_operacji["kryt1"] = KryteriumSylwestera("kryt1",
                                                                self.historia_obiektow["macierz7"])
        self.historia_operacji["kryt2"] = KryteriumSylwestera("kryt2",
                                                                self.historia_obiektow["macierz8"])
        self.historia_operacji["kryt3"] = KryteriumSylwestera("kryt3",
                                                                self.historia_obiektow["macierz9"])
    def display_menu():
        clear_terminal()
        print("------------MENU-GŁÓWNE-----------------")
        print("1. Zarządzanie pamięcią")
        print("2. Dodawanie macierzy")
        print("3. Odejmowanie macierzy")
        print("4. Mnożenie macierzy przez skalar")
        print("5. Mnożenie macierzy")
        print("6. Eliminacja Gaussa")
        print("7. Wyznacznik")
        print("8. Kryterium Sylwestera")
        print("9. Wyjście")
        print("Podaj liczbę:   ", end="")


    def run(self):
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
                operacja = MnozeniePrzezSkalar.enter_num_m(self.historia_obiektow)
                operacja.print_and_save(self)
            elif (user_input == "5"):
                operacja = Mnozenie.enter_m_m(self.historia_obiektow)
                operacja.print_and_save(self)
            elif (user_input == "6"):
                operacja = EliminacjaGaussa.enter_m(self.historia_obiektow)
                operacja.print_and_save(self)
            elif (user_input == "7"):
                operacja = Wyznacznik.enter_m(self.historia_obiektow)
                operacja.print_and_save(self)
            elif (user_input == "8"):
                operacja = KryteriumSylwestera.enter_m(self.historia_obiektow)
                operacja.print_and_save(self)
            elif (user_input == "9"):
                break
            else:
                invalid_input("Podano niepoprawne dane")


            
            
