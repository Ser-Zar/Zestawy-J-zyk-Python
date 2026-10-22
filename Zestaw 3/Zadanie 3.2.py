# L = [3, 5, 4] ; L = L.sort()

# Metoda list.sort() sortuje listę w miejscu i zwraca None. 
# Przypisanie wyniku z powrotem do L niszczy listę i ustawia L = None. Powinno być samo L.sort() lub L = sorted(L).

# x, y = 1, 2, 3

# Błąd rozpakowywania (ValueError: too many values to unpack). 
# Po prawej stronie są 3 wartości, a po lewej tylko 2 zmienne.

# X = 1, 2, 3 ; X[1] = 4

# Zmienna X staje się krotką (tuple). Krotki są niemutowalne (immutable), 
# więc próba przypisania elementu rzuca TypeError: 
# 'tuple' object does not support item assignment.

# X = [1, 2, 3] ; X[3] = 4

# Indeks poza zakresem (IndexError: list assignment index out of range). 
# Lista ma 3 elementy (indeksy 0, 1, 2), więc indeks 3 nie istnieje. 
# Nowy element dodaje się przez X.append(4).

# X = "abc" ; X.append("d")

# Napisy (str) nie mają metody .append(), są niemutowalne 
# (AttributeError: 'str' object has no attribute 'append'). 
# Należy użyć konkatenacji: X = X + "d".

# L = list(map(pow, range(8)))

# Błąd argumentów (TypeError: pow expected at least 2 arguments, got 1). 
# Funkcja wbudowana pow(base, exp) wymaga co najmniej dwóch argumentów, 
# a range(8) przekazuje tylko jeden element na wywołanie.