line = "Ala ma kota"
# Długości: Ala (3), ma (2), kota (4) -> 3 + 2 + 4 = 9

result = sum(len(w) for w in line.split())
expected_result = 9
assert result == expected_result