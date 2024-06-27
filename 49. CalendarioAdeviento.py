import datetime as dt

"""
EASY
 * ¿Conoces el calendario de adviento de la comunidad (https://adviento.dev)?
 * 24 días, 24 regalos sorpresa relacionados con desarrollo de software,
 * ciencia y tecnología desde el 1 de diciembre.
 *
 * Enunciado: Crea una función que reciba un objeto de tipo "Date" y retorne
 * lo siguiente:
 * - Si la fecha coincide con el calendario de aDEViento 2022: Retornará el regalo
 *   de ese día (a tu elección) y cuánto queda para que finalice el sorteo de ese día.
 * - Si la fecha es anterior: Cuánto queda para que comience el calendario.
 * - Si la fecha es posterior: Cuánto tiempo ha pasado desde que ha finalizado.
 *
 * Notas:
 * - Tenemos en cuenta que cada día del calendario comienza a medianoche 00:00:00
 *   y finaliza a las 23:59:59.
 * - Debemos trabajar con fechas que tengan año, mes, día, horas, minutos
 *   y segundos.
"""

def calendar(fecha):
    cal = {
        1:"Git y Github",
        2:"Aprende Python",
        3:"SQL",
        4:"El Programador Pragmático",
        5:"Patrones de Diseño",
        6:"Jetpack Compose",
        7:"Aprendiendo JavaScript",
        8:"Cracking the Coding Interview",
        9:"SQL en un fin de semana",
        10:"Aprende HTML",
        11:"Hack 4 u",
        12:"Desarrollo de apps",
        13:"Clean JavaScript",
        14:"Ralola Networks",
        15:"Disño Agil con TDD",
        16:"El último programador",
        17:"Docker",
        18:"Codigo Sostenible",
        19:"Flutter",
        20:"Stream Deck",
        21:"Aprendiendo React",
        22:"La atersania del código limpio",
        23:"Curso Intensivo de Python",
        24:"Git y Github",
    }
    
    inicioCal = dt.datetime(2023, 12, 1)
    finalCal = dt.datetime(2023, 12, 25)

    if fecha < inicioCal:
        remainingTime = inicioCal-fecha
        return "Falta "+str(remainingTime)+" para que comience"
    elif inicioCal <= fecha <= finalCal:
        dia = (fecha-inicioCal).days+1
        final = dt.datetime(fecha.year, fecha.month, fecha.day, 23, 59, 59)
        return "You won "+str(cal.get(dia, "No hay premio p causa"))
    else:
        passTime = fecha-finalCal
        return "Ha pasado "+str(passTime)+" desde que acabo"

print(calendar(dt.datetime(2023, 12, 4)))
print(calendar(dt.datetime(2023, 5, 17)))
print(calendar(dt.datetime(2024, 6, 26)))
