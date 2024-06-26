"""
EASY
 * Crea una función que ordene y retorne una matriz de números.
 * - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
 *   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
 *   o de mayor a menor.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
 *   automáticamente.
"""

def ordenar_lista(lista, orden):
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if (orden == "Asc" and lista[j] > lista[j+1]) or (orden == "Desc" and lista[j] < lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
    
    return lista

lista = [4, 9, 6, 2, 8]
print(ordenar_lista(lista, "Asc"))