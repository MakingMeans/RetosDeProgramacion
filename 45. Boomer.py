"""
EASY
 * Crea una función que retorne el número total de bumeranes de
 * un array de números enteros e imprima cada uno de ellos.
 * - Un bumerán (búmeran, boomerang) es una secuencia formada por 3 números
 *   seguidos, en el que el primero y el último son iguales, y el segundo
 *   es diferente. Por ejemplo [2, 1, 2].
 * - En el array [2, 1, 2, 3, 3, 4, 2, 4] hay 2 bumeranes ([2, 1, 2]
 *   y [4, 2, 4]).
"""

def boomer(nums):
    boomers = []

    for i in range (len(nums)-2):
        if (nums[i] == nums[i+2] and nums[i] != nums[i+1]):
            temp = nums[i:i+3]
            boomers.append(temp)

    return boomers

print(boomer([2, 1, 2, 3, 3, 4, 2, 4, 5, 4]))