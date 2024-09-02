#!/usr/bin/env python3

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def main():
    try:
        number = int(input(""))
        if number < 0:
            print("El factorial no está definido para números negativos.")
        else:
            f = factorial(number)
            print(f"{f}")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
if __name__ == "__main__":
    main()