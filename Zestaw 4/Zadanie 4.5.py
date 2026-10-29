def odwracanie(L, left, right):
    if not isinstance(L, list):
        raise ValueError("Pierwszym argumentem musi być lista.")
    if not isinstance(left, int) or not isinstance(right, int):
        raise ValueError("Indeksy muszą być liczbami całkowitymi.")
    if left < 0 or right >= len(L):
        raise ValueError("Indeksy wykraczają poza zakres listy.")
    
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


# Asercja / test z naturalnym przykładem (lista przedmiotów w plecaku)
ekwipunek = ["latarka", "termos", "mapa", "kompas", "scyzoryk", "lina"]
# Odwracamy od indeksu 1 do 4: ["termos", "mapa", "kompas", "scyzoryk"]
odwracanie(ekwipunek, 1, 4)
assert ekwipunek == ["latarka", "scyzoryk", "kompas", "mapa", "termos", "lina"]