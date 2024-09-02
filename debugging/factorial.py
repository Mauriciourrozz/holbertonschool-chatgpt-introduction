import sys

def factorial(n):
    if n == 0:
        return 1
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) < 2:
    print("Error: No se proporcionó ningún argumento.")
    sys.exit(1)

try:
    n = int(sys.argv[1])
    if n < 0:
        print("Error: El número debe ser un entero no negativo.")
        sys.exit(1)
    f = factorial(n)
    print(f)
except ValueError:
    print("Error: El argumento debe ser un número entero.")
    sys.exit(1)
