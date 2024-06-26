"""
EASY
 * Crea una función que transforme grados Celsius en Fahrenheit
 * y viceversa.
 *
 * - Para que un dato de entrada sea correcto debe poseer un símbolo "°"
 *   y su unidad ("C" o "F").
 * - En caso contrario retornará un error.
"""

def convertir_temperatura(temperatura):
    valor, unidad = int(temperatura[:-2]), temperatura[-1]
    if unidad == 'C':
        return str((valor * 9/5) + 32) + "°F"
    elif unidad == 'F':
        return str((valor - 32) * 5/9) + "°C"
    else:
        return "DUH esa unidad no esta soportada por el code"

print(convertir_temperatura("100°C"))
