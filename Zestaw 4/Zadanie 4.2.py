def make_ruler(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Długość miarki musi być nieujemną liczbą całkowitą.")
    
    top = "|" + "....|" * n
    bottom = "0"
    for i in range(1, n + 1):
        label = str(i)
        bottom += " " * (5 - len(label)) + label
    
    return top + "\n" + bottom


def make_grid(rows, cols):
    if not isinstance(rows, int) or not isinstance(cols, int) or rows < 1 or cols < 1:
        raise ValueError("Liczba wierszy i kolumn musi być dodatnią liczbą całkowitą.")
    
    horiz = "+---" * cols + "+"
    vert = "|   " * cols + "|"
    
    lines = []
    for _ in range(rows):
        lines.append(horiz)
        lines.append(vert)
    lines.append(horiz)
    
    return "\n".join(lines)


# Asercje / testy
expected_ruler_3 = "|....|....|....|\n0    1    2    3"
assert make_ruler(3) == expected_ruler_3

expected_grid_2x2 = "+---+---+\n|   |   |\n+---+---+\n|   |   |\n+---+---+"
assert make_grid(2, 2) == expected_grid_2x2