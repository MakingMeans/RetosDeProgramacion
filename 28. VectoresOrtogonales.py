"""
EASY
 * Crea un programa que determine si dos vectores son ortogonales.
 * - Los dos array deben tener la misma longitud.
 * - Cada vector se podría representar como un array. Ejemplo: [1, -2]
"""

def ortogonal(vec1, vec2):
    if (len(vec1) != len(vec2)):
        return("Vectores no compatibles!")
    else:
        resultado = 0
        for i in range(len(vec1)):
            resultado += vec1[i]*vec2[i]
        
        if (resultado == 0):
            print("Los vectores son ortogonales!")
        else: 
            print("Los vectores no son ortogonales!")

ortogonal([1,-2],[2,1])