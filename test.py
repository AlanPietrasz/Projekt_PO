
# import pandas as pd
# from colorama import Fore, Style

# def print_dataframe_with_color(df, row, col, color):
#     # Znalezienie maksymalnej długości liczby dziesiętnej w ramce danych
#     max_width = df.astype(str).apply(lambda x: x.str.len()).max().max()

#     # Wypisanie ramki danych z wyróżnioną komórką
#     for i in range(df.shape[0]):
#         for j in range(df.shape[1]):
#             if i == row and j == col:
#                 print(f"{color}{str(df.iloc[i, j]).ljust(max_width)}{Style.RESET_ALL}", end=" ")
#             else:
#                 print(str(df.iloc[i, j]).ljust(max_width), end=" ")
#         print()

# # Przykładowa ramka danych
# data = {'A': [1, 2, 3, 4, 5],
#         'B': [6, 7, 8, 900000000000000000000000, 10],
#         'C': [11, 12, 13, 14, 15]}
# df = pd.DataFrame(data)

# # Wywołanie funkcji print_dataframe_with_color z wyróżnioną komórką (1, 1) na zielono
# print_dataframe_with_color(df, 1, 1, Fore.GREEN)


# import numpy as np
# from colorama import Fore, Style

# def print_dataframe_with_color(arr, row, col, color):
#     # Znalezienie maksymalnej długości liczby dziesiętnej w macierzy
#     max_width = np.vectorize(lambda x: len(str(x)))(arr).max()

#     # Wypisanie macierzy z wyróżnioną komórką
#     for i in range(arr.shape[0]):
#         for j in range(arr.shape[1]):
#             if i == row and j == col:
#                 print(f"{color}{str(arr[i, j]).ljust(max_width)}{Style.RESET_ALL}", end=" ")
#             else:
#                 print(str(arr[i, j]).ljust(max_width), end=" ")
#         print()

# # Przykładowa macierz danych
# data = {'A': [1, 2, 3, 4, 5],
#         'B': [6, 7, 8, 9000000, 10],
#         'C': [11, 12, 13, 14, 15]}
# arr = np.array(list(data.values())).T

# # Wywołanie funkcji print_dataframe_with_color z wyróżnioną komórką (1, 1) na zielono
# print_dataframe_with_color(arr, 1, 1, Fore.GREEN)


import numpy as np
from colorama import Fore, Style

def print_dataframe_with_color(arr, row, col, color):
    # Znalezienie maksymalnej długości liczby dziesiętnej w macierzy
    max_width = np.vectorize(lambda x: len(str(x)))(arr).max()
    n_length = len(str(self.n))
    m_length = len(str(self.m))
    # Wypisanie indeksów kolumn
    print(" " * 6, end="")
    for j in range(arr.shape[1]):
        print(f"({j})", end=" " * (max_width - 3))
    print()

    # Wypisanie macierzy z wyróżnioną komórką
    for i in range(arr.shape[0]):
        # Wypisanie indeksu wiersza
        print(f"({i}):", end=" ")
        for j in range(arr.shape[1]):
            if i == row and j == col:
                print(f"{color}{str(arr[i, j]).ljust(max_width)}{Style.RESET_ALL}", end=" ")
            else:
                print(str(arr[i, j]).ljust(max_width), end=" ")
        print()

   

# Przykładowa macierz danych
data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 90000000000000, 10],
        'C': [11, 12, 13, 14, 15],
        'D': [11, 12, 13, 14, 15]}
arr = np.array(list(data.values())).T

# Wywołanie funkcji print_dataframe_with_color z wyróżnioną komórką (1, 1) na zielono
print_dataframe_with_color(arr, 1, 1, Fore.GREEN)

