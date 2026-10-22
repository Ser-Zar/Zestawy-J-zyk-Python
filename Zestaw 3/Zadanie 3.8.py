# Przykładowe nietypowe sekwencje: mix typów i powtórzeń
ciag_a = ["bit", 77, "bajt", 13, 77, "omega"]
ciag_b = [77, "alfa", 999, "omega", "bit", 13]

# (a) Elementy wspólne w obu sekwencjach
wspolne = list(set(ciag_a) & set(ciag_b))

# (b) Suma zbiorów obu sekwencji (wszystkie unikalne elementy)
wszystkie = list(set(ciag_a) | set(ciag_b))

print("Wspólne:", wspolne)
print("Wszystkie:", wszystkie)