import os

from macierz import Macierz


class Menu:

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
        
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    def invalid_input():
        print()
        print("Podano niepoprawne dane")
        user_input = input()
        Menu.clear_terminal()


    def run():
        while (True):
            Menu.display_menu()
            user_input = input()
            if (user_input == "1"):
                while (True):
                    Menu.display_memory_menu()
                    user_input = input()
                    if (user_input == "1"):
                        """
                        TODO
                        """
                        pass
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


            
            
