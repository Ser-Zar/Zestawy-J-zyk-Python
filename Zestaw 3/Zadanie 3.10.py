# Sposób 1: Klasyczny literał słownikowy
slownik_1 = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

# Sposób 2: dict() z parami klucz-wartość (zip dwóch list)
litery = ["I", "V", "X", "L", "C", "D", "M"]
wartosci = [1, 5, 10, 50, 100, 500, 1000]
slownik_2 = dict(zip(litery, wartosci))

# Sposób 3: Konstruktor dict z argumentami nazwanymi
slownik_3 = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)


def roman2int(roman: str) -> int:
    tabela = slownik_1
    suma = 0
    poprzednia = 0
    
    # Przechodzenie od prawej do lewej upraszcza logikę odejmowania (np. IV, IX)
    for znak in reversed(roman.upper()):
        wartosc = tabela[znak]
        if wartosc < poprzednia:
            suma -= wartosc
        else:
            suma += wartosc
            poprzednia = wartosc
            
    return suma

# Testy
for test in ["MCMXCIV", "CDXLIV", "MMXXIV"]:
    print(f"{test} -> {roman2int(test)}")