# import tkinter as tk
# import numpy as np

# def wczytaj_macierz():
#     rozmiar_label.config(text="Podaj rozmiar macierzy:")
#     n_entry.config(state=tk.NORMAL)
#     m_entry.config(state=tk.NORMAL)
#     wprowadz_button.config(state=tk.NORMAL)

# def wprowadz_dane():
#     n = int(n_entry.get())
#     m = int(m_entry.get())
#     macierz_label.config(text="Wprowadź macierz:")
#     macierz_entry = []
#     for i in range(n):
#         row = []
#         for j in range(m):
#             entry = tk.Entry(root, width=10)
#             entry.grid(row=i+4, column=j)
#             row.append(entry)
#         macierz_entry.append(row)
    
#     oblicz_button = tk.Button(root, text="Oblicz macierz odwrotną", command=lambda: oblicz_odwrotna(macierz_entry))
#     oblicz_button.grid(row=n+4, column=0, columnspan=m)
    
# def oblicz_odwrotna(macierz_entry):
#     macierz = []
#     for row in macierz_entry:
#         row_vals = []
#         for entry in row:
#             row_vals.append(int(entry.get()))
#         macierz.append(row_vals)
    
#     try:
#         odwrotna = np.linalg.inv(macierz)
#         wynik_label.config(text="Macierz odwrotna:")
#         wynik_entry = []
#         for i in range(len(odwrotna)):
#             row = []
#             for j in range(len(odwrotna[0])):
#                 entry = tk.Entry(root, width=10)
#                 entry.insert(tk.END, str(odwrotna[i][j]))
#                 entry.config(state=tk.DISABLED)
#                 entry.grid(row=i+7, column=j)
#                 row.append(entry)
#             wynik_entry.append(row)
#     except np.linalg.LinAlgError:
#         wynik_label.config(text="Macierz nie jest odwracalna.")

# root = tk.Tk()

# wczytaj_button = tk.Button(root, text="Wczytaj macierz", command=wczytaj_macierz)
# wczytaj_button.grid(row=0, column=0)

# rozmiar_label = tk.Label(root, text="")
# rozmiar_label.grid(row=1, column=0)

# n_entry = tk.Entry(root, width=10, state=tk.DISABLED)
# n_entry.grid(row=2, column=0)

# m_entry = tk.Entry(root, width=10, state=tk.DISABLED)
# m_entry.grid(row=2, column=1)

# wprowadz_button = tk.Button(root, text="Wprowadź dane", command=wprowadz_dane, state=tk.DISABLED)
# wprowadz_button.grid(row=3, column=0)

# macierz_label = tk.Label(root, text="")
# macierz_label.grid(row=4, column=0)

# wynik_label = tk.Label(root, text="")
# wynik_label.grid(row=6, column=0)

# root.mainloop()







# import tkinter as tk
# import numpy as np

# def wczytaj_macierz():
#     rozmiar_label.config(text="Podaj rozmiar macierzy:")
#     n_entry.config(state=tk.NORMAL)
#     m_entry.config(state=tk.NORMAL)
#     wprowadz_button.config(state=tk.NORMAL)

# def wprowadz_dane():
#     n = int(n_entry.get())
#     m = int(m_entry.get())
#     macierz_label.config(text="Wprowadź macierz:")
#     macierz_entry = []
#     for i in range(n):
#         row = []
#         for j in range(m):
#             entry = tk.Entry(root, width=10)
#             entry.grid(row=i+4, column=j)
#             row.append(entry)
#         macierz_entry.append(row)
    
#     oblicz_button = tk.Button(root, text="Oblicz macierz odwrotną", command=lambda: oblicz_odwrotna(macierz_entry, n, m))
#     oblicz_button.grid(row=n+4, column=0, columnspan=m)
    
# def oblicz_odwrotna(macierz_entry, n, m):
#     macierz = []
#     for row in macierz_entry:
#         row_vals = []
#         for entry in row:
#             row_vals.append(int(entry.get()))
#         macierz.append(row_vals)
    
#     try:
#         odwrotna = np.linalg.inv(macierz)
#         wynik_label.config(text="Macierz odwrotna:")
#         wynik_entry = []
#         for i in range(len(odwrotna)):
#             row = []
#             for j in range(len(odwrotna[0])):
#                 entry = tk.Entry(root, width=10)
#                 entry.insert(tk.END, str(odwrotna[i][j]))
#                 entry.config(state=tk.DISABLED)
#                 entry.grid(row=i+7, column=j)
#                 row.append(entry)
#             wynik_entry.append(row)
        
#         # Usunięcie pól tekstowych zawierających wynik
#         for row in wynik_entry:
#             for entry in row:
#                 entry.destroy()
        
#         # Przywrócenie stanu początkowego programu
#         rozmiar_label.config(text="")
#         n_entry.delete(0, tk.END)
#         n_entry.config(state=tk.DISABLED)
#         m_entry.delete(0, tk.END)
#         m_entry.config(state=tk.DISABLED)
#         wprowadz_button.config(state=tk.DISABLED)
#         macierz_label.config(text="")
#     except np.linalg.LinAlgError:
#         wynik_label.config(text="Macierz nie jest odwracalna.")

# root = tk.Tk()

# wczytaj_button = tk.Button(root, text="Wczytaj macierz", command=wczytaj_macierz)
# wczytaj_button.grid(row=0, column=0)

# rozmiar_label = tk.Label(root, text="")
# rozmiar_label.grid(row=1, column=0)

# n_entry = tk.Entry(root, width=10, state=tk.DISABLED)
# n_entry.grid(row=2, column=0)

# m_entry = tk.Entry(root, width=10, state=tk.DISABLED)
# m_entry.grid(row=2, column=1)

# wprowadz_button = tk.Button(root, text="Wprowadź dane", command=wprowadz_dane, state=tk.DISABLED)
# wprowadz_button.grid(row=3, column=0)

# macierz_label = tk.Label(root, text="")
# macierz_label.grid(row=4, column=0)

# wynik_label = tk.Label(root, text="")
# wynik_label.grid(row=6, column=0)

# root.mainloop()






import tkinter as tk
import numpy as np

def wczytaj_macierz():
    rozmiar_label.config(text="Podaj rozmiar macierzy:")
    n_entry.config(state=tk.NORMAL)
    m_entry.config(state=tk.NORMAL)
    wprowadz_button.config(state=tk.NORMAL)

def wprowadz_dane():
    n = int(n_entry.get())
    m = int(m_entry.get())
    macierz_label.config(text="Wprowadź macierz:")
    macierz_entry = []
    for i in range(n):
        row = []
        for j in range(m):
            entry = tk.Entry(root, width=10)
            entry.grid(row=i+4, column=j)
            entry.bind('<Return>', lambda event, row=i, column=j: wprowadz_wartosc(event, row, column, macierz_entry))
            row.append(entry)
        macierz_entry.append(row)
    
    oblicz_button = tk.Button(root, text="Oblicz macierz odwrotną", command=lambda: oblicz_odwrotna(macierz_entry))
    oblicz_button.grid(row=n+4, column=0, columnspan=m)
    
def wprowadz_wartosc(event, row, column, macierz_entry):
    if row < len(macierz_entry) and column < len(macierz_entry[0]):
        current_entry = macierz_entry[row][column]
        next_row = row + (column + 1) // len(macierz_entry[0])
        next_column = (column + 1) % len(macierz_entry[0])
        if current_entry.get().strip() != '':
            macierz_entry[row][column].delete(0, tk.END)
            macierz_entry[next_row][next_column].focus_set()
    
def oblicz_odwrotna(macierz_entry):
    macierz = []
    for row in macierz_entry:
        row_vals = []
        for entry in row:
            row_vals.append(int(entry.get()))
        macierz.append(row_vals)
    
    try:
        odwrotna = np.linalg.inv(macierz)
        wynik_label.config(text="Macierz odwrotna:")
        wynik_entry = []
        for i in range(len(odwrotna)):
            row = []
            for j in range(len(odwrotna[0])):
                entry = tk.Entry(root, width=10)
                entry.insert(tk.END, str(odwrotna[i][j]))
                entry.config(state=tk.DISABLED)
                entry.grid(row=i+7, column=j)
                row.append(entry)
            wynik_entry.append(row)
        
        # Usunięcie pól tekstowych zawierających wynik
        for row in wynik_entry:
            for entry in row:
                entry.destroy()
        
        # Przywrócenie stanu początkowego programu
        rozmiar_label.config(text="")
        n_entry.delete(0, tk.END)
        n_entry.config(state=tk.DISABLED)
        m_entry.delete(0, tk.END)
        m_entry.config(state=tk.DISABLED)
        wprowadz_button.config(state=tk.DISABLED)
        macierz_label.config(text="")
    except np.linalg.LinAlgError:
        wynik_label.config(text="Macierz nie jest odwracalna.")

root = tk.Tk()

wczytaj_button = tk.Button(root, text="Wczytaj macierz", command=wczytaj_macierz)
wczytaj_button.grid(row=0, column=0)

rozmiar_label = tk.Label(root, text="")
rozmiar_label.grid(row=1, column=0)

n_entry = tk.Entry(root, width=10, state=tk.DISABLED)
n_entry.grid(row=2, column=0)

m_entry = tk.Entry(root, width=10, state=tk.DISABLED)
m_entry.grid(row=2, column=1)

wprowadz_button = tk.Button(root, text="Wprowadź dane", command=wprowadz_dane, state=tk.DISABLED)
wprowadz_button.grid(row=3, column=0)

macierz_label = tk.Label(root, text="")
macierz_label.grid(row=4, column=0)

wynik_label = tk.Label(root, text="")
wynik_label.grid(row=6, column=0)

root.mainloop()
