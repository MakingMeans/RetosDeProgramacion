"""
EASY
 * Crea una función que sea capaz de encriptar y desencriptar texto
 * utilizando el algoritmo de encriptación de Karaca
 * (debes buscar información sobre él).
"""
#reemplazos = {'a': '0', 'e': '1', 'i': '2', 'o': '3', 'u': '4'}

def encriptar(text):
    text = text.lower()
    text = text[::-1]
    text = text.replace('a', '0').replace('e', '1').replace('i', '2').replace('o', '3').replace('u', '4')
    text += "aca"
    return text

texto = "Hola Wenas"
texto = encriptar(texto)
print(texto)

def desencriptar(text):
    text = text[:-3]
    text = text[::-1]
    text = text.replace('0', 'a').replace('1', 'e').replace('2', 'i').replace('3', 'o').replace('4', 'u')
    return text

texto = desencriptar(texto)
print(texto)
