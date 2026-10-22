# Fragment 1 

# x = 2; y = 3;
# if (x > y):
#     result = x;
# else:
#     result = y;

# poprawny składniowo

# Fragment 2 

# for i in "axby": if ord(i) < 100: print (i)

#  niepoprawny składniowo - Błąd składniowy (SyntaxError: invalid syntax)
# Dlaczego? - W jednej linii po dwukropku nie można łączyć instrukcji złożonych (for, if). 
# Instrukcja if musi znaleźć się w nowej, wciętej linii pod pętlą for.

# Fragment 3

# for i in "axby": print (ord(i) if ord(i) < 100 else i)

#  poprawny składniowo