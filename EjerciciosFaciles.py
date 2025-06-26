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

