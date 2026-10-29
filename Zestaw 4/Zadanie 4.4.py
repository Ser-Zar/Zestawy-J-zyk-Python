def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Indeks ciągu Fibonacciego musi być nieujemną liczbą całkowitą.")
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

assert fibonacci(10) == 55