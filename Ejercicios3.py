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


# Crear un programa que permita calcular el importe de compra total
# si iguala o supera los $100 se genera un número aleatorio de 1 a 5
# donde cada valor corresponde un color, blanco sin descuento
# roja 10%, azul 20%, verde 25%, amarilla 50%. Mostrar el importe final

import random

def descuentos():

	importe = int(input('INTRODUZCA EL TOTAL DE SU COMPRA: '))
	dictColor = {'COLOR:': 'DESCUENTO:', 'BOLA BLANCA': 'NO TIENE', 'BOLA ROJA': '10 POR CIENTO', 
				'BOLA AZUL': '20 POR CIENTO', 'BOLA VERDE': '25 POR CIENTO', 'BOLA AMARILLA': '50 POR CIENTO'}



	if importe >= 100:

		print('SU GASTO IGUALA O SUPERA LOS $100.00 POR LO TANTO TIENE DESCUENTO')
		for k, v in dictColor.items():
			print(k.ljust(25, ' ') + v.rjust(10))

		colorBall = random.randint(1, 5)

		if colorBall == 1:

			print('No tiene descuento. Su total a pagar es', importe)

		elif colorBall == 2:
 
			print('ALEATORIAMENTE OBTUVO UNA BOLA ROJA')
			print('FELCIDADES, HA GANADO UN 10 POR CIENTO DE DESCUENTO')
			print('SU NUEVO TOTAL A PAGAR ES: ' + '$' + str(importe - round(importe/10, 2)))

		elif colorBall == 3:

			print('ALEATORIAMENTE OBTUVO UNA BOLA AZUL')
			print('FELCIDADES, HA GANADO UN 20 POR CIENTO DE DESCUENTO')
			print('SU NUEVO TOTAL A PAGAR ES: ' + '$' + str(importe - round(importe/5, 2)))

		elif colorBall == 4:

			print('ALEATORIAMENTE OBTUVO UNA BOLA VERDE')
			print('FELCIDADES, HA GANADO UN 25 POR CIENTO DE DESCUENTO')
			print('SU NUEVO TOTAL A PAGAR ES: ' + '$' + str(importe - round(importe/4, 2)))

		else:

			print('ALEATORIAMENTE OBTUVO UNA BOLA AMARILLA')
			print('FELCIDADES, HA GANADO UN 50 POR CIENTO DE DESCUENTO')
			print('SU NUEVO TOTAL A PAGAR ES: ' + '$' + str(importe - round(importe/2, 2)))

	else:

		print('SU TOTAL A PAGAR ES DE: ', importe)

descuentos()



# Crear un programa que devuelva el total a pagar donde el
# usuario debe elegir el producto por codigo seguna la tabla

def main():

	productoCodigo = {'CAMISA': 1, 'CINTURON': 2, 'ZAPATOS': 3,
					  'PANTALON': 4, 'CALCETINES': 5, 'FALDAS':6,
					  'GORRAS': 7, 'SUETER': 8, 'CORBATA': 9, 'CHAQUETA': 10}

	print('ELIJA EL PRODUCTO DESEADO:')
	print()
	print('PRODUCTO' + 18*" " + 'CODIGO')
	print()
	for k, v in productoCodigo.items():
		print(k.ljust(30, '.') + (str(v).rjust(2)))

	relacion = {1: 35, 2: 10, 3: 50, 4: 40, 5: 5, 6: 20, 7: 7, 8: 15, 9: 10, 10: 35}

	codigoProducto = {1: 'CAMISA', 2: 'CINTURON', 3: 'ZAPATOS', 4: 'PANTALON', 5: 'CALCETINES',
					  6: 'FALDAS', 7: 'GORRAS', 8: 'SUETER', 9: 'CORBATA', 10: 'CHAQUETA'}

	dictCompras = {}

	continuar = 's'

	listaUnidades = []

	compraTotal = 0

	while continuar.lower() == 's':

		totalProd = 0

		cod = int(input('INTRODUZCA EL CÓDIGO: '))

		print('EL PRECIO ES DE $' + str(relacion[cod]))

		unidades = int(input('INTRODUZCA EL NÚMERO DE UNIDADES: '))

		totalProd = float(unidades * relacion[cod])

		print('Total de {} por {} unidades es ${} '.format(codigoProducto[cod], unidades, totalProd))
		print()

		dictCompras[codigoProducto[cod]] = totalProd

		listaUnidades.append(unidades)

		continuar = input('DESEA CONTINUAR SI(S) O NO(N): ')
		print()

		compraTotal += totalProd

	i = 0

	print()
	print('U ' + 'PRODUCTO' + 21 * " " + 'TOTAL')

	for x, z in dictCompras.items():

		print(str(listaUnidades[i]) + ' ' + x.ljust(29, '.') + '$' + (str(z).rjust(2)))

		i += 1

	print()
	print('TOTAL......................... $', compraTotal)

main()
'''


# El scrip debe calcular el importe por el alquiler de la pelicula más
# el recargo por demora en devolución segun la tabla dada

def backToThePast():

	print("=======================================================")
	print("CATEGORIA       PRECIO  CODIGO  RECARGO/DIA DE ATRASO")
	print("")
	print("FAVORITOS        $2.50     1             $0.50")
	print("NUEVOS           $3.00     2             $0.75")
	print("ESTRENOS         $3.50     3             $1.00")
	print("SUPER ESTRENOS   $4.00     4             $1.50")
	print("=======================================================")
	print("")

	salir = ''

	while salir != 1:

		catPeli = int(input('INTRODUZCA EL CÓDIGO DE LA PELICULA: '))

		diasAtraso = int(input('INTRODUZCA EL NÚMERO DE DÍAS DE ATRASO EN LA DEVOLUCIÓN: '))

		print()

		if catPeli == 1:

			monto = 2.50+(diasAtraso*0.50)

			print('EL TOTAL A PAGAR ES ${0:.2f} DOLARES'.format(monto))

		elif catPeli == 2:

			monto = 3.00+(diasAtraso*0.75)

			print('EL TOTAL A PAGAR ES ${0:.2f} DOLARES'.format(monto))

		elif catPeli == 3:

			monto = 3.50+(diasAtraso*1.00)

			print('EL TOTAL A PAGAR ES ${0:.2f} DOLARES'.format(monto))

		elif catPeli == 4:

			monto = 4.00+(diasAtraso*1.50)

			print('EL TOTAL A PAGAR ES ${0:.2f} DOLARES'.format(monto))

		else:

			print('POR FAVOR INTRODUZCA EL CODIGO CORRECTO.')
			print()

		try:
			print('#######################################')
			salir = int(input('SI DESEA SALIR PRESIONE 1 DE LO CONTRARIO OTRO NÚMERO: '))

		except ValueError:

			print('POR FAVOR INTRODUZCA UN NÚMERO!')
			print('#######################################')

backToThePast()