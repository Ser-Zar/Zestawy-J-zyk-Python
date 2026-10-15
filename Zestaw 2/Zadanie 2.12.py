line = "Kto pyta nie bladzi nigdy"
wyrazy = line.split()

result_first = "".join(w[0] for w in wyrazy)
expected_first = "Kpnbn"
assert result_first == expected_first

result_last = "".join(w[-1] for w in wyrazy)
expected_last = "oaeiy"
assert result_last == expected_last