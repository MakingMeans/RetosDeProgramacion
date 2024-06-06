"""
EASY
 * Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes
 *   de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes
 *   de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
"""

def conjuntos(list1,list2,trigger):
    finalList = []
    if trigger:
        if len(list1)<len(list2):
            for element in list1:
                if element in list2:
                    finalList.append(element)
        else:
            for element in list2:
                if element in list1:
                    finalList.append(element)
    else:
        for element in list1:
            if element not in list2:
                finalList.append(element)
        for element in list2:
            if element not in list1:
                finalList.append(element)
            
    return finalList

print(conjuntos(['papa','mamamia','works'],['patata','pollo','papa'],False))