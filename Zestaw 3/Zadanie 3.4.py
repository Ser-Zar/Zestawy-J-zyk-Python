while True:
    dane = input("Podaj liczbę (lub 'stop' aby zakończyć): ").strip()
    if dane.lower() == "stop":
        break
    try:
        x = float(dane)
        print(f"Liczba: {x}, Trzecia potęga: {x**3}")
    except ValueError:
        print(f"Błąd: '{dane}' nie daje się przekonwertować na float.")