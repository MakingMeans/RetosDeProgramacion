"""
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información
 * al respecto.

 * Un número narcisista es aquel que es igual a la suma de sus dígitos elevados 
 * a la potencia de su número de cifras.
"""

def numNar(n):
    n_str = str(n)

    r = 0
    for i in n_str:
        r += int(i)**len(n_str)

    if r==int(n_str):
        print("El número es Narcisista!")
    else: print("El número no es Narcisista!")

numNar(2)