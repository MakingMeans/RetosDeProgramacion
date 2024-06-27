"""
EASY
 * Crea un función que reciba un texto y retorne la vocal que
 * más veces se repita.
 * - Ten cuidado con algunos casos especiales.
 * - Si no hay vocales podrá devolver vacío.
"""

def miVocal(text):
    vocals = {
        "a":0,
        "e":0, 
        "i":0, 
        "o":0, 
        "u":0
    }

    text = text.lower()

    for i in text:
        if i in vocals.keys():
            vocals[i] += 1

    vocalFav = []
    maxCont = 0
            
    for letra, i in vocals.items():
        if i > maxCont:
            maxCont = i
            vocalFav.clear()
            vocalFav.append(letra)
        elif i == maxCont:
            vocalFav.append(letra)
        
    print(str(vocalFav)+" se repite "+str(maxCont)+" veces.")


miVocal("No me gusta tu tono de piel...")