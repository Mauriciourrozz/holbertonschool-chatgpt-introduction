def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    try:
        number = int(input("Ingrese un número para calcular su factorial: "))
        if number < 0:
            print("El factorial no está definido para números negativos.")
        else:
            f = factorial(number)
            print(f"El factorial de {number} es {f}.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
