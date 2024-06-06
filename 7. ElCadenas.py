"""
EASY
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def invertirChars(text):
    inverted = ""
    for char in text:
        inverted = char+inverted
    return inverted

print(invertirChars("I hate Ospina"))