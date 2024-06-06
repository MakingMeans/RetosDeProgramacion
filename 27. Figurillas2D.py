"""
EASY
 * Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 * - EXTRA: ¿Eres capaz de dibujar más figuras? (tambienn pueden ser simbolos. EJ: un simbolo representativo)
"""

# print("* ***\n* *  \n*****\n  * *\n*** *")

def cuadrado(n):
    for i in range(n):
        if (i == 0 or i == n-1):
            print("* "*n)
        else:
            print("* " + ("  " * int(n-2)) + "*")
        
def triangulo1(n):
    for i in range(n):
        if (i==0):
            print(("  " * (int(n)-1)) + ("* ") + ("  " * (int(n)-1)))
        elif (i == n-1):
            print("* "*((int(n)*2)-1))
        else:
            print("  "*(int(n)-1-i)+"* "+"  "*((i*2)-1)+"* "+"  " * (int(n)-1-i))

def triangulo2(n):
    for i in range(1, n+1):
        if i==1 or i==n:
            print("* "*i)
        else:
            print("* "+"  "*(i-2)+"*")

cuadrado(5)
triangulo1(5)
triangulo2(5)