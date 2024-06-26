"""
EASY
 * Crea una función que calcule el valor del parámetro perdido
 * correspondiente a la ley de Ohm.
 * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará
 *   el valor del tercero (redondeado a 2 decimales).
 * - Si los parámetros son incorrectos o insuficientes, la función retornará
 *   la cadena de texto "Invalid values".
"""

def leyDeOhm(V=-1,I=-1,R=-1):
    parameters = [V,I,R]
    if max(parameters)==-1:
        print("Invalid values")
    elif min(parameters)>-1:
        print("Invalid values")
    elif ((V==I==-1)or(V==R==-1)or(I==R==-1)):
        print("Invalid values")
    elif V==-1:
        V = round(R * I, 2)
        print(str(V)+"(V)")
    elif I==-1:
        I = round(V / R, 2)
        print(str(I)+"(A)")
    elif R==-1:
        R = round(V / I, 2)
        print(str(R)+"(Ohm)")

leyDeOhm(V=10, R=5)