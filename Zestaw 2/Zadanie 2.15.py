L = [421, 3, 87, 590]

result = "".join(str(x) for x in L)
expected_result = "421387590"
assert result == expected_result