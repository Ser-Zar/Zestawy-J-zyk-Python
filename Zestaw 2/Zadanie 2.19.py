# Uzupełnienie do 3 cyfr zerami z lewej: 8 -> 008, 41 -> 041, 620 -> 620, 2 -> 002, 19 -> 019
L = [8, 41, 620, 2, 19]

result = "".join(str(x).zfill(3) for x in L)
expected_result = "008041620002019"
assert result == expected_result