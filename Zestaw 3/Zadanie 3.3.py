# Wariant 1: pętla for
print("Pętla for:")
for num in range(31):
    if num % 3 == 0:
        continue
    print(num, end=" ")
print()

# Wariant 2: pętla while
print("Pętla while:")
val = 0
while val <= 30:
    if val % 3 != 0:
        print(val, end=" ")
    val += 1
print()