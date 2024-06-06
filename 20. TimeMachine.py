"""
EASY
 * Crea una función que reciba días, horas, minutos y segundos (como enteros)
 * y retorne su resultado en milisegundos.
"""

# Asumiendo que la entrada es: dd:hh:mm:ss <-- con separación por ":"

def converter(time):
    time = time.split(":")
    finalTime = 0
    if time[0]!=0:
        finalTime += int(time[0])*24*60*60*1000
    if time[1]!=0:
        finalTime += int(time[1])*60*60*1000
    if time[2]!=0:
        finalTime += int(time[2])*60*1000
    if time[3]!=0:
        finalTime += int(time[3])*1000
    return finalTime

print(converter("12:01:54:27"))
    
