line = """Kurs jezyka Python
jest\t interesujacy
i praktyczny"""

result = len(line.split())
expected_result = 7
assert result == expected_result