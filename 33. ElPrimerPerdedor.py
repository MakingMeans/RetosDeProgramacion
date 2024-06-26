"""
EASY
 * Dado un listado de números, encuentra el SEGUNDO más grande
"""

def elSegundo(numbers):
    max = 0
    sec = 0
    
    for i in range(len(numbers)):
        if numbers[i]>max:
            sec,max = max,numbers[i]
        if numbers[i]<max and numbers[i]>sec:
            sec = numbers[i]
    print(sec)

elSegundo([7,6,8,9])