"""
EASY
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
"""

def capitalize(txt:str):
    new_text=""
    txt=txt.split(" ")
    
    for word in txt:
        char = word[0].upper()
        new_text += char+word[1:]+" "
    
    return new_text

print(capitalize("mamawebo con pola"))