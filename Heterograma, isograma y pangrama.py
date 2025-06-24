# /*
#  * Crea 3 funciones, cada una encargada de detectar si una cadena de
#  * texto es un heterograma, un isograma o un pangrama.
#  * - Debes buscar la definición de cada uno de estos términos.
#  */

def heterograma():
    palabra = input("Ingrese una palabra o una frase:\n")
    if palabra != palabra:
        print("Es un heterograma")
    else:
        print("No es un heterograma")

heterograma()