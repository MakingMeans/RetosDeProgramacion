""""
HARD
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""

def fiboP(n,M):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fiboMEMO(n-1,M)+fiboMEMO(n-2,M)

def fiboMEMO(n,M):
    if (n) in M.keys():
        return M[(n)]
    M[(n)]=fiboP(n,M)
    return M[(n)]

M={}

print(fiboP(50,M))