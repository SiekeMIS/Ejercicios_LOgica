# /*
#  * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
#  * Ejemplos:
#  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#  */

import math

def EsPrimo_EsFibonacci_EsPar(numero):
    resultado = f"{numero}"
    #Es Primo
    if numero > 1:
        for indice in range(2, numero):
            if numero % indice == 0:
                resultado += " no es primo, "
                break
        else: resultado += " es primo, "
    else: resultado += " no es primo, "

    #Es Fibonacci
    resultado += "es fibonacci" if numero > 0 and (is_perfect_square(5 * numero * numero + 4) or is_perfect_square(5 * numero * numero - 4 )) else "no es fibonacci"

    #Es Par
    resultado += " es par" if numero %2 == 0 else " es impar"

    print(resultado)

def is_perfect_square(number):
    sqrt = int(math.sqrt(number))
    return sqrt * sqrt == number

EsPrimo_EsFibonacci_EsPar(5)
EsPrimo_EsFibonacci_EsPar(0)