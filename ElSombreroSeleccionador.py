# /*
#  * Crea un programa que simule el comportamiento del sombrero seleccionador del
#  * universo mágico de Harry Potter.
#  * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
#  * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
#  * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
#  *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
#  * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
#  *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
#  */

# Gryffindor: Valor
# Slytherin: Ambición
# Hufflepuff: Lealtad
# Ravenclaw: Sabiduria

class PreguntasSombrero:
    def __init__(self, pregunta, respuestas):
        self.pregunta = pregunta
        self.respuestas = respuestas

preguntas_sombrero = [PreguntasSombrero("¿Cómo te definirías?", [
                                       ("1.Valiente", "Gryffindor"), 
                                       ("2.lealtad", "Hufflepuff"), 
                                       ("3.Sabio", "Ravenclaw"), 
                                       ("4.Ambicioso", "Slytherin")]),

                      PreguntasSombrero("¿Cual es tu clase favorita?", [
                                       ("1.Vuelo", "Gryffindor"), 
                                       ("2.Animales Fantasticos", "Hufflepuff"), 
                                       ("3.Pociones", "Ravenclaw"), 
                                       ("4.Defensa contra las artes oscuras", "Slytherin")])]

for pregunta_sombrero in preguntas_sombrero:
    
    print(pregunta_sombrero.pregunta)
    for respuesta in pregunta_sombrero.respuestas:
        print(respuesta[0])
    
    input("Responde 1, 2, 3 o 4:")
    if respuesta =="1" or respuesta == 