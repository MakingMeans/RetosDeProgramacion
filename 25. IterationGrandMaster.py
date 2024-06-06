"""
EASY
 * Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
 * ¿De cuántas maneras eres capaz de hacerlo?
 * Crea el código para cada una de ellas.
"""

def method1():
    for i in range(1,101):
        print(i)

method1()

def method2():
    i=1
    while (i<=100):
        print(i)
        i = i+1

method2()

def method3(n):
    if n>100:
        return
    print(n)
    method3(n+1)

method3(1)

def method4():
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)
    print(6)
    print(7)
    print(8)
    print(9)
    print(10)
    print(11)
    print(12)
    print(13)
    print(14)
    print(15)
    print(16)
    print(17)
    print(18)
    print(19)
    print(20)
    print("blah blah blah more numbers almendra")
    print(100)