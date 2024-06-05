"""
EASY
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */
"""

def bin(n):
    if n == 0:
        return 0
    
    bin = ""

    while(n > 0):
        bin = str(n%2) + bin
        n = n//2

    return bin

print(bin(25))