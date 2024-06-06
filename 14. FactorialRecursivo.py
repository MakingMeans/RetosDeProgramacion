"""
EASY
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
"""

def facRecurssive(index, n=1):
    if index == 0:
        return n
    n = n*index
    return facRecurssive(index-1, n)

print(facRecurssive(5))