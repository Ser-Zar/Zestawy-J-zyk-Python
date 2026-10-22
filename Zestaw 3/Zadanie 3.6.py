kolumny = 5  # x
wiersze = 3   # y

segment_poziomy = "+---" * kolumny + "+"
segment_pionowy = "|   " * kolumny + "|"

linie = []
for _ in range(wiersze):
    linie.append(segment_poziomy)
    linie.append(segment_pionowy)
linie.append(segment_poziomy)

siatka = "\n".join(linie)
print(siatka)