# Długości wyrazów: W (1), lesie (5), roslo (5), wiele (5), grzybow (7)
line = "W lesie roslo wiele grzybow"
wyrazy = line.split()

# (a) najdłuższy wyraz
result_a = max(wyrazy, key=len)
expected_a = "grzybow"
assert result_a == expected_a

# (b) długość najdłuższego wyrazu
result_b = len(result_a)
expected_b = 7
assert result_b == expected_b