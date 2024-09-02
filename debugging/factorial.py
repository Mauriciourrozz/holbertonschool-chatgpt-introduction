import sys

def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) != 2:
    print("Por favor, proporciona un único número entero como argumento.")
    sys.exit(1)

try:
    num = int(sys.argv[1])
    if num < 0:
        raise ValueError
except ValueError:
    print("Por favor, proporciona un número entero positivo.")
    sys.exit(1)

f = factorial(num)
print(f)