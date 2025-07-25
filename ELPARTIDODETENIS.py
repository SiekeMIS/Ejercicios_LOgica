# /*
#  * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#  * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
#  * gane cada punto del juego.
#  * 
#  * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#  * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#  *   15 - Love
#  *   30 - Love
#  *   30 - 15
#  *   30 - 30
#  *   40 - 30
#  *   Deuce
#  *   Ventaja P1
#  *   Ha ganado el P1
#  * - Si quieres, puedes controlar errores en la entrada de datos.   
#  * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
#  */

from enum import Enum


class Player(Enum):
    P1 = 1
    P2 = 2


def tenis_game(points: list):

    game = ["Love", "15", "30", "40"]
    p1_points = 0
    p2_points = 0
    finished = False
    error = False

    for player in points:

        error = finished

        p1_points += 1 if player == Player.P1 else 0
        p2_points += 1 if player == Player.P2 else 0

        if p1_points >= 3 and p2_points >= 3:
            if not finished and abs(p1_points - p2_points) <= 1:
                print("Deuce" if p1_points == p2_points else
                      "Ventaja P1" if p1_points > p2_points else "Ventaja P2")
            else:
                finished = True
        else:
            if p1_points < 4 and p2_points < 4:
                print(f"{game[p1_points]} - {game[p2_points]}")
            else:
                finished = True

    print("Los puntos jugados no son correctos" if error or not finished else
          "Ha ganado el P1" if p1_points > p2_points else "Ha ganado el P2")


tenis_game([Player.P1, Player.P1, Player.P2, Player.P2,
           Player.P1, Player.P2, Player.P1, Player.P1])

tenis_game([Player.P1, Player.P1, Player.P2, Player.P2,
           Player.P1, Player.P2, Player.P1, Player.P1, Player.P2, Player.P1])

tenis_game([Player.P1, Player.P1, Player.P1, Player.P1, Player.P1, Player.P1])

tenis_game([Player.P1, Player.P1])