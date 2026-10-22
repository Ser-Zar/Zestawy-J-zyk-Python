dlugosc = 14  # parametr miarki

pasek_gorny = "|" + "....|" * dlugosc
pasek_dolny = ""

for i in range(dlugosc + 1):
    etykieta = str(i)
    if i == 0:
        pasek_dolny += etykieta
    else:
        # Odstęp uwzględnia długość liczby, by ostatnia cyfra trafiła pod '|'
        pasek_dolny += " " * (5 - len(etykieta)) + etykieta

miarka = pasek_gorny + "\n" + pasek_dolny
print(miarka)