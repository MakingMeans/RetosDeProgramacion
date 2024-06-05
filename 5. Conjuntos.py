"""
EASY
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
"""

def conjuntos(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    out1, out2 = "", ""

    for char in str1:
        if char not in str2 and char not in out1:
            out1 = out1+char
    
    for char in str2:
        if char not in str1 and char not in out2:
            out2 = out2+char
    
    return out1,out2

out1,out2 = conjuntos("Clado de pollo","Papas fritas")
print(out1 + "\n" + out2)