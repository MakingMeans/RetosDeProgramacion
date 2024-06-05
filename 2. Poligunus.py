""""
EASY
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 """

def area (l,b,h):
    if (l<3 or l>4): print("No esta soportado!")

    if (l==3):
        print("El área del triangulo es: " + str((b*h)/2))
    elif (b==h):
        print("El área del cuadrado es: " + str(b*h))
    else:
        print("El área del rectangulo es: " + str(b*h))

area(4,5,3)
area(4,3,3)
area(3,7,4)