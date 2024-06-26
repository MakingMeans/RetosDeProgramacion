"""
EASY
 * Crea una función que reciba un texto y muestre cada palabra en una línea,
 * formando un marco rectangular de asteriscos.
 * - ¿Qué te parece el reto? Se vería así:
 *   **********
 *   * ¿Qué   *
 *   * te     *
 *   * parece *
 *   * el     *
 *   * reto?  *
 *   **********
"""

def marco(frase):
    frase = frase.split(" ")

    max = 0
    for i in range(len(frase)):
        if (len(frase[i])>max):
            max = len(frase[i])

    print("*"*(max+4)) 
    for i in range(len(frase)):
        dif = len(frase[i])
        print("* "+frase[i]+(" "*(max-dif))+" *")
    print("*"*(max+4)) 

marco("Quiero hacer un cartel del minecra... PDS: Odio a Ospina :D")