# /*
#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)
#  */
import random

def password(longitud, mayusculas, numero, simbolos):
    if longitud >= 16 and longitud <= 8:
        return "Error"

    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    if mayusculas:
        alfabeto += "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    if simbolos:
        alfabeto += "!#$%&/=_:;-.,"
    if numero:
        alfabeto += "1234567890"
    
    contraseña = []
    for _ in range(longitud):
        eleccion = random.choice(alfabeto)
        contraseña.append(eleccion)
    return ''.join(contraseña)

print(password(16, True, True, True))