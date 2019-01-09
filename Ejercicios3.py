'''
# El juego consistirá en adivinar una cadena de números distintos.
# Al principio, el programa debe pedir la longitud de la cadena (de 2 a 9 cifras).
# Después el programa debe ir pidiendo que intentes adivinar la cadena de números.
# En cada intento, el programa informará de cuántos números han sido acertados
# (el programa considerará que se ha acertado un número si coincide el valor y la posición).

import random


def masterMind():
    long = int(input("Dime la longitud de la cadena: "))
    numSecret = ""
    while len(numSecret) < long:
        dig = str(random.randrange(10))
        numSecret += dig

    num = input('Intenta adivinar la cadena: ')
    aciertos = 0

    while numSecret != num:

        for i in numSecret:
            x = 0
            if i == num[x]:
                aciertos += 1
                x += 1
        if len(numSecret) == aciertos:
            print('Con', num, 'has adivinado', aciertos, 'valores. Felicidades')
            break
        else:
            print('Con', num, 'has adivinado', aciertos, 'valores.')
            num = input('Intenta adivinar la cadena')


masterMind()



# Escribe un programa que pida dos palabras y diga si riman o no.
# Si coinciden las tres últimas letras tiene que decir que riman.
# Si coinciden sólo las dos últimas tiene que decir que riman un poco
# y si no, que no riman.


def rimando():

    pal1 = input('Ingresa la 1ra palabra: ')
    pal2 = input('Ingresa la segunda palabra: ')

    if pal1[-1] == pal2[-1] and pal1[-2] == pal2[-2] and pal1[-3] == pal2[-3]:

        print('Las palabras riman!')

    elif pal1[-1] == pal2[-1] and pal1[-2] == pal2[-2]:

        print('Las palabras riman poco')

    else:

        print('No riman')

rimando()



# Has un programa que pida al usuario una cantidad de dolares,
# una tasa de interés y un numero de años. Muestra por pantalla
# en cuanto se habrá convertido el capital inicial transcurridos
# esos años si cada año se aplica la tasa de interés introducida.

def capFinal():

    capInicial = int(input('Introduce el capital inicial: '))
    tasaInteres = float(input('Introduce la tasa de interes: '))
    anos = int(input('Introduce la cantidad de años: '))

    capFinal = round(capInicial * (1 + tasaInteres / 100) ** anos, 2)

    return capFinal

print(capFinal())
'''

# Crear un programa que permita calcular el importe de compra total
# si iguala o supera los $100 se genera un número aleatorio de 1 a 5
# donde cada valor corresponde un color, blanco sin descuento
# roja 10%, azul 20%, verde 25%, amarilla 50%. Mostrar el importe final

import random

def descuentos():

	importe = int(input('INTRODUZCA EL TOTAL DE SU COMPRA: '))

	if importe >= 100:

		print('SU GASTO IGUALA O SUPERA LOS $100.00 POR LO TANTO TIENE DESCUENTO')

	else:

		print('SU TOTAL A PAGAR ES DE: ', importe)

descuentos()