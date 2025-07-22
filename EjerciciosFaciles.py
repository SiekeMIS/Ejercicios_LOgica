# """
# Sumar dos numeros y mostrar su resultado (1)
# """
# def suma():
#     numUno = int(input("Ingrese un Numero:\n"))
#     numDos = int(input("Ingrese otro numero:\n"))
#     print(f"Resultado:\n{numUno + numDos}")

# suma()

# """
# Calcule el area de un circulo con un radio dado (2)
# """
# import math

# def AreaCirculo():
#     radio = int(input("Ingrese el readio del de la circunferencia:\n"))
#     pi = math.pi
#     area = pi * radio**2
#     print(f"El Area de la Circunferencia es:\n {area}")

# AreaCirculo()

# """
# Concatena dos cadenas de texto (3)
# """
# def concatenar():
#     textoUno = input("Ingresa el primer texto:\n")
#     textoDos = input("Ingresar el segundotexto:\n")
#     print(f"Resultado:\n{textoUno + " " + textoDos}")

# concatenar()

# """
# Crear lista  con diferentes elementos e imprimirla (4)
# """
# lista = ["Fieos", "Salsa", "Carne Molida", "Cebolla", "Zanaoria", "Vino", "Azucar", "Queso Parmesano"]
# print(lista)

# """
# Realiza una multiplicación de dos numeros y muestra el resultado (5)
# """
# def multiplicación():
#     numeroUno = int(input("Ingrese el primer numero:\n"))
#     numeroDos = int(input("Ingrese el segundo numero:\n"))
#     print(f"Resultado: {numeroUno * numeroDos}")
# multiplicación()

# """
# Crea una cadena de texto y muestra su longitud (6)
# """
# def longitud():
#     cadena = input("Ingrese la cadena:\n")
#     largo = len(cadena)
#     print(largo)
# longitud()

# """
# Calcula el promedio de una lista de numeros (7)
# """
# def promedio():
#     Lista_Numeros = [25, 56, 79, 130, 1024]
#     suma = sum(Lista_Numeros)
#     promedio = suma / len(Lista_Numeros)
#     print(promedio)
# promedio()

# """
# Crea una tupla con elementos e imprimela (8)
# """
# Tupla = ([1, 2], [5, "Manzana"])
# print(Tupla)

# """
# Realiza la potencia de un numero (9)
# """
# import math

# def potencia():
#     base = int(input("Ingrese un numero como base de la potencia:\n"))
#     exponente = int(input("Ingrese un numero como exponente de la potencia:\n"))
#     resultado = math.pow(base, exponente)
#     print(resultado)
# potencia()

# """
# Invertir una cadena (10)
# """
# def cadena_inversa():
#     cadena = input("Ingrese una cadena:\n")
#     cadena_invertida = cadena[::-1]
#     print(cadena_invertida)
# cadena_inversa()

# """
# Calcula el área de un rectángulo, pide base y altura al usuario
# """

# def area_rectangulo():
#     largo = int(input("Ingrese el Largo del rectangulo:\n"))
#     ancho = int(input("Ingrse el ancho del rectangulo:\n"))
#     area = largo * ancho
#     print(f"El area del rectangulo es:\n{area}")
# area_rectangulo()

# """
# Convierte un numero entero en casena (12)
# """
# def entero_a_cadena():
#     numero_entero = int(input("Ingrese un Numero entero:\n"))
#     numero_entero_dos = int(input("Ingrese un Numero entero:\n"))
#     cadena_dos = str(numero_entero_dos)
#     cadena = str(numero_entero)
#     print(cadena + cadena_dos)
# entero_a_cadena()

# """
# Reemplaza un caracter en una cadena (13)
# """
# def reemplazar():
#     cadena = "Hola Bduno!"
#     caracter_a_reemplzar = "a"
#     nueva_letra = "6"
#     remplazo = cadena.replace(caracter_a_reemplzar, nueva_letra)
#     print(remplazo)
# reemplazar()

# """
# Pasa una cadena de Mayúsculas a Minúsculas (14)
# """
# def MayAMin():
#     cadena_mayuscula = str(input("Ingresa una cadena en Mayúscula:\n"))
#     cadena_minuscula = cadena_mayuscula.lower()
#     print(f"Cadena pasada  minuscula:\n{cadena_minuscula}")
# MayAMin()

# """
# Ordena una lista de numeros de menor a mayor (15)
# """
# def lista_ordenada():
#     lista_desordenada = [8, 12, 4, 1, 0, 54, 33, 11, 13, 69]
#     print(f"Lista Desordenada\n{lista_desordenada}")
#     lista_desordenada.sort()
#     print(f"Lista Ordenada:\n{lista_desordenada}")
# lista_ordenada()

# """
# Calcula 2 elevado a la 4a potencia sin utilizar el operador ** (16)
# """
# import math

# def potencia():
#     base = 2
#     exponente = 4
#     potencia = math.pow(base, exponente)
#     print(potencia)
# potencia()

# """
# Extrae una subcadena de una cadena dada (17)
# """
# def subcadena():
#     cadena = "Que salga pega"
#     print(cadena[10:14])
# subcadena()

# """
# Convierte un número decimal a un número entero (18)
# """
# def numero_decimal_a_entero():
#     numero = 3.14
#     print(int(numero))
# numero_decimal_a_entero()

# """
# Cuenta las concurrencias de un carácter especifico de una cadena (19)
# """
# def concurrencias_cadena():
#     cadena = str(input("Ingrese una cadena:\n"))
#     concurrencias = cadena.count("a")
#     print(f"La cantidad de a es:\n{concurrencias}")
# concurrencias_cadena()

# """
# Encuentra y muestra el ultimo carácter de una cadena (20)
# """
# def UltiumoCaracter():
#     cadena = str(input("Ingrese una cadena:\n"))
#     ultimo_caracter = cadena[-1]
#     print(f"El ultimo caracter es:\n{ultimo_caracter}")
# UltiumoCaracter()

# """
# Multiplica una cadena por un número entero (21)
# """
# def multiplicar_cadena():
#     cadena = str(input("Ingresa una cadena:\n"))
#     multiplicacion = cadena *2
#     print(f"Resultado:\n{multiplicacion}")
# multiplicar_cadena() 

# """
# Divide una cadena en una lista de subcadenas (22)
# """
# def cadena_a_subcadenas():
#     cadena = str(input("Ingrese un texto:\n"))
#     lista = cadena.split()
#     print(f"Lista:\n{lista}")
# cadena_a_subcadenas()

# """
# Verifica que una palabra es un palindromo (23)
# """
# def palindromo():
#     cadena = str(input("Ingrese una palabra:\n"))
#     print(cadena[::-1])
#     if cadena == cadena[::-1]:
#         print("Si es un palindromo")
#     else:
#         print("No es un palindomo")
# palindromo()

# """
# Elimina un elemento especifico de una lista (24)
# """
# def eliminar_de_lista():
#     lista = [1, 2, "peyito"]
#     lista.remove("peyito")
#     print(lista)
# eliminar_de_lista()

# """
# Genera una lista de números de 1 al 200 (25)
# """
# def genera_numeros():
#     lista = []
#     for i in range(1, 201):
#         lista.append(i)
#     print(lista)
# genera_numeros()

# """
# o
# """
# lista = list(range(1, 201))
# print(lista)

# """
# intercambia los valores de dos variables con asignación míltiple(26)
# """
# def intercambio_variables():
#     a =int(input("Ingrese el valor de a:\n"))
#     b = int(input("Ingrese el valor de b:\n"))
#     a, b = b, a
#     print(f"El valor de a es:\n{a}")
#     print(f"El valor de b es:\n{b}")
# intercambio_variables()

# """
# Realiza operaciones básicas con conjuntos union e interseccion (27)
# """
# def operraciones_conjuntas_inter():
#     conjunto_a ={1, 2, 3, 4, 5}
#     conjunto_b = {4, 5, 6, 7, 8}
#     union = conjunto_a.union(conjunto_b) #o tambien se puede usar conjunto_a | conjunto_b
#     intersección = conjunto_a.intersection(conjunto_b) # intersección = conjunto_a & conjunto_b
#     print(union)
#     print(intersección)
# operraciones_conjuntas_inter()

# """
# Extrae un elemento especifico de una tupla (28)
# """
# def extraer_elemnto_de_tupla():
#     tupla = ([1, 2], [3, 4], [5, 6])
#     elemto_extraido = tupla[2][1] #Extraera el elemento 6 de la tupla
#     print(f"El elemento extraido es:\n{elemto_extraido}")
# extraer_elemnto_de_tupla()

# """
# Combina dos listas en pares usando la función zip (29)
# """
# def combinar_listas():
#     lista1 = ['Bruno', 'Nala', 'Peyin', 'Peya Loca']
#     lista2 = [1, 2, 3, 4]
#     lista_emparejada = list(zip(lista1, lista2))
#     print(f"Lista en pares:\n{lista_emparejada}")
# combinar_listas()

# """
# Elimina duplicados en una lista (30)
# """
# def eliminar_duplicados():
#     lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9]
#     lista_singular = list(set(lista))
#     print(f"Lista sin duplicados:\n{lista_singular}")
# eliminar_duplicados()

# """
# Pide un numero y Verifica si es positivo, negativo o cero. (31)
# """
# def verificar_numero():
#     numero = int(input("Ingrese un numero:\n"))
#     if numero > 0:
#         print("El numero es positivo")
#     elif numero < 0:
#         print("El numero es negativo")
#     else:
#         print("El numero es cero")
# verificar_numero()

# """
# Pide un numero y comprueba si es par o impar, utiliza if y modulo (32)
# """
# def par_o_impar():
#     numero = int(input("Ingrese un numero:\n"))
#     if numero %2==0:
#         print("El numero es par")
#     else:
#         print("El numero es impar")
# par_o_impar()

# """
# Determna si un año es bisiesto.
# Regla de negocio:
# - Divisible por 4.
# - No divisible por 100.
# - Divisible por 400. (33)
# """
# def es_bisiesto():
#     año = int(input("Ingrese un año:\n"))
#     if año %4==0 and (año %100 !=0 or año %400 ==0):
#         print(f"El año {año} es bisiesto")
#     else:
#         print(f"El año {año} no es bisiesto")
# es_bisiesto()

# """
# Verifica si una cadena es mayor o igual a 10 caracteres (34)
# """
# def verifica_cadena():
#     cadena = str(input("Ingresa una cadena:\n"))
#     cantidad = len(cadena)
#     # print(cantidad)
#     if cantidad >= 10:
#         print(f"La cadena tiene {cantidad}, por ende, 10 o mas caracteres")
#     else:
#         print(f"{cantidad} La cadena tiene menos de 10 caracteres")
# verifica_cadena()

# """
# Comprueba si un número está en el rango de 1 a 100 (35)
# """
# def comprobar_rango():
#     numero = float(input("Ingrese un Numero:\n"))
#     if numero >= 1 and (numero <= 100):
#         print(f"El numero {numero} esta dentro del rango")
#     else:
#         print(f"El numero {numero} está fuera del rango")
# comprobar_rango()

# """
# Pide un caracter y Determina si es una vocal (36)
# """
# def es_vocal():
#     caracter = str(input("ingrese un caracter:\n")).lower()
#     if caracter in "aeiou":
#         print("Este caracter es una vocal")
#     else:
#         print("No es una vocal")
# es_vocal()

# """
# Calcula el maximo de tres numeros (37)
# """
# def maximo_tres_numeros():
#     numeroUno = int(input("Ingrese el primer numero:\n"))
#     numeroDos = int(input("Ingrese el segundo numero:\n"))
#     numeroTres = int(input("Ingrese el tercer numero:\n"))
#     maximo = max(numeroUno, numeroDos, numeroTres)
#     print(f"El numero maximo es:\n{maximo}")
# maximo_tres_numeros()

# """
# Determina si un numero es divisible por 5 y 7 (38)
# """
# def divisible_cinco_siete():
# 	numero = int(input("ingrese un numero:\n"))
# 	if numero % 7 == 0 and (numero % 5 == 0):
# 		print(f"El numero {numero} es divisible por 5 y 7 ")
# 	else:
# 		print("El numero no es divisible por 5 ni por 7")
# divisible_cinco_siete()

# """
# Verifica si la palabra ingresada es python (39)
# """
# def verificar_python():
# 	palabra = str(input("Ingrese la palabra python:\n")).lower()
# 	if palabra == "python":
# 		print("La palabra ingresa es python")
# 	else:
# 		print("La palabra ingresada NO es python")
# verificar_python()

# """
# Calcular el IMC e interpretarlo (40)
# """
# def IMC():
# 	peso = float(input("Ingrese su peso:\n"))
# 	estatura = float(input("Ingrese su estatura en metro y centimetro (ejemplo  1.70):\n"))
# 	estatura_centimetros = estatura * 100  # Convertir a centimetros
# 	imc = peso / (estatura_centimetros/100)**2
# 	print(f"Tu IMC es: {imc}")
# 	if imc <= 18.5:
# 		print("Tu IMC indica que estas Bajo peso.")
# 	elif imc > 18.5 and imc <= 24.5:
# 		print("Tu IMC indica que tu peso es saludable.")
# 	elif imc > 25 and imc <= 30:
# 		print ("Tu IMC indica que estas con sobrepeso.")
# 	elif imc >= 30:
# 		print("Tu IMC indica que estas Obeso.")
# IMC()

# """
# Imprime los numero del 10 al 1 en orden descendente (41)
# """
# def imprimir_desc():
# 	for i in range(10, 0, -3):
# 		print(i) 
# imprimir_desc()

# """
# Solicita al usario ingresar un numero N y luego imprime la suma de todos los numero desde 1 hasta N (42)
# """
# def suma_n():
# 	n = int(input("Ingrese un numero:\n"))
# 	suma = sum(range(1, n+1))
# 	print(f"La suma de de los numero del 1 hasta {n} es: {suma}")
# suma_n()

# """
# Solicita al usario ingresar un numero N e imprime el factorial de ese numero (43)
# """
# import math
# def factorial_descendente():
# 	n = int(input("Ingrese un numero:\n"))
# 	if n > 0:
# 		print (f"El factorial de {n} es:\n{math.factorial(n)}")
# 	else:
# 		print("El numero debe ser mayor a 1")
# factorial_descendente()

# """
# Genera un número aleatorio entre 1 y 10. Luego, pie al usuario adivinar el número hasta que lo haga correctamente. (44)
# """
# import random
# def numero_aleatorio():
# 	while True:
# 		numero = random.randint(1, 10)
# 		intento = int(input("Intenta elegir el Numero Correcto:\n"))
# 		if intento == numero:
# 			print(f"Le achuntaste, Amiga eri seca el numero era {numero}")
# 			break
# 		else:
# 			print(f"Error el numero {intento} no es el correcto, de seguro eres onvre.")
# numero_aleatorio()

# """
# imprime la tabla de multiplicar de cada numero ingresado por el usuario (45)
# """
# def tabla_multiplicar():
# 	numero = int(input("Ingresa un numero:\n"))
# 	i = 1
# 	while i <= 12:
# 		print(f"{numero} x {i} = {numero * i}")
# 		i = i + 1
# tabla_multiplicar()

# """
# Solicita al usuario ingresar un número y cuenta cuántos dígitos tiene. (46)
# """
# def contar_digitos():
# 	numero = int(input("Ingrese una cifra numérica:\n"))
# 	numero_cadena = str(numero)
# 	if numero > 0:
# 		cantidad = len(numero_cadena)
# 		print(f"Cantidad de dígitos en la cifra:\n{cantidad}")
# 	else:
#             print("El numero debe ser mayor a 0")
# contar_digitos()

# """
# Hacer un menu de opciones que incluya la opción de salir del programa. (47)
# """
# def menu():
# 	while True:
# 		print("Bienvenido al super menú de Lucas")
# 		print("Ingrese una de las siguientes opciones:\n")
# 		print("1 para ordenar algo")
# 		print("2 para ir al baño")
# 		print("3 para salir")
# 		opcion = int(input("Ingrese el numero aquí:\n"))
# 		if opcion == 3:
# 			print("Haslta luego...")
# 			break
# 		elif opcion == 2 or opcion == 1:
# 			print("OKis")
# 		else:
# 			if opcion != 1 and opcion != 2 and opcion != 3:
# 				print("Por favor eliga una opcion valida\n")
# menu()

# """
# Simular un lanzamiento de dado hasta obtener un 6 (48)
# """
# import random
# def lazar_dado():
# 	while True:
# 		dado = random.randint(1, 6)
# 		if dado == 6:
# 			print(f"El numero es {dado}, listeke!")
# 			break
# 		else:
# 			print(f"ups, salio {dado},otra vez")
# lazar_dado()

# """
# Mostrar los números del 1 al 100 pero reemplazando los múltiplos de 3 por "Fizz" y los múltiplos de 5 por "Buzz" (49)
# """
# def FizzBuzz():
# 	for i in range(1, 101):
# 		if i % 3 == 0 and (i % 5 == 0):
# 			print("FizzBuzz")
# 		elif i % 3 == 0:
# 			print("Fizz")
# 		elif i % 5 == 0:
# 			print("Buzz") 
# 		else:
# 			print(i)
# FizzBuzz()

