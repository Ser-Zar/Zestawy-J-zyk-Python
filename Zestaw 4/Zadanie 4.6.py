def sum_seq(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise ValueError("Argument musi być listą lub krotką.")
    
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += sum_seq(item)
        elif isinstance(item, (int, float)):
            total += item
        else:
            raise ValueError(f"Nieobsługiwany typ elementu w sekwencji: {type(item)}")
    return total


# Asercja / test (np. zagnieżdżone punkty/wagi w grze planszowej)
punkty_graczy = [12, (5, [3, 10]), [], [4, (1, 5)]]
assert sum_seq(punkty_graczy) == 40