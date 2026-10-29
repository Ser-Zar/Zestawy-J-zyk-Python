def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Silnia jest zdefiniowana tylko dla nieujemnych liczb całkowitych.")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

assert factorial(6) == 720
assert factorial(0) == 1