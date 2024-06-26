"""
EASY
 * Crea una función que imprima los 30 próximos años bisiestos
 * siguientes a uno dado.
 * - Utiliza el menor número de líneas para resolver el ejercicio.
"""

def añoBisiestoLaSecuela(año):
    bisiestos = []
    while len(bisiestos) < 30:
        if len(bisiestos) == 0:
            año +=1
        else:
            año +=4
        if(año%4==0 and año%100!=0) or (año%400==0):
            bisiestos.append(año)
    print(bisiestos)

añoBisiestoLaSecuela(2021)