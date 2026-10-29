def flatten(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise ValueError("Argument wejściowy musi być listą lub krotką.")
    
    flat_list = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


# Asercja / test z różnymi typami danych (np. struktura działów w firmie i ich kodów)
struktura_projektu = ["Core", ["API", ("Auth", "DB")], [], [["Cache"]], "Frontend"]
assert flatten(struktura_projektu) == ["Core", "API", "Auth", "DB", "Cache", "Frontend"]