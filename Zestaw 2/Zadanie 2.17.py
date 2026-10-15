line = "samolot rower hulajnoga auto statek"
wyrazy = line.split()

# 1. Alfabetycznie (bez rozróżniania wielkości liter)
result_alpha = sorted(wyrazy, key=str.lower)
expected_alpha = ["auto", "hulajnoga", "rower", "samolot", "statek"]
assert result_alpha == expected_alpha

# 2. Względem długości:
# auto (4), rower (5), statek (6), samolot (7), hulajnoga (9)
result_length = sorted(wyrazy, key=len)
expected_length = ["auto", "rower", "statek", "samolot", "hulajnoga"]
assert result_length == expected_length