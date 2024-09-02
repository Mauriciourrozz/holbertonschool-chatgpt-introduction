#!/usr/bin/python3
import sys
"""
    Calcula el factorial de un número entero no negativo utilizando recursión.

    Parámetros:
    n (int): Un número entero no negativo del cual se calculará el factorial.

    Devoluciones:
    int: El resultado del factorial de n.
    """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)