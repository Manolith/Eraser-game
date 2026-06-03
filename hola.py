import random
import time
from textwrap import dedent


def main():
    language = int(input("Welcome!\nSelect a language\n1-English\n2-Spanish\n"))
    clean_terminal()
    while not 0 < language < 3:
        language = int(input("Select a valid option: "))

    if language == 1:
        english()
    else:
        spanish()


def spanish():
    instructions_es()


def english():
    instructions_en()


def instructions_en():
    option = 0
    iText = """
    1- What is Eraser?
    2- How to play.
    3- Start the game.

    """
    while option != 3:
        print("Welcome to Eraser anime version!")
        print(iText)
        option = int(input("Select a option: "))

        # to validate option input
        while not 0 < option < 4:
            option = int(input("Select a valid option: "))

        clean_terminal()

        if option == 1:
            qText = dedent("""
                Eraser is a board game created by the Spanish designer Ignasi Ferré and illustrated by Raúl Rojas.

                In this game for 3 to 6 players, participants must guess concepts using clues that disappear each round.
                All players have to guess the same concept from one of five categories (One Piece, Naruto, Dragon Ball, Spokon, and Isekai),
                but each player receives one fewer clue than the previous player.

                This game is a simplified and customized adaptation of the original Eraser.
                It reduces the number of concepts and the overall playtime while preserving the core essence of the original creators' design.

                """)

            print(qText)
            input("Press Enter to continue...")
            clean_terminal()

        elif option == 2:
            insText = dedent(
                """

            -The starting player must choose a category and will be assigned a concept.
            They must then write clues according to the number of players in the game.
            -The next player receives a list of clues written by the player who was assigned the concept.
            They must try to guess the concept and write down their answer. Finally, they must remove one clue, so the following player receives fewer clues.
            -The game continues following the same process until it is once again the turn of the player who was assigned the concept.

            """
            )
            eText = dedent(
                """



            """
            )
            pText = dedent(
                """



            """
            )

            print(insText)
            input("Press Enter to continue...")
            print(eText)
            input("Press Enter to continue...")
            print(pText)
            input("Press Enter to exit...")
            clean_terminal()


def instructions_es():
    option = 0
    iText = """
    1- ¿Qué es Eraser?
    2- ¿Cómo se juega?
    3- Comenzar el juego.

    """
    while option != 3:
        print("¡Bienvenido a Eraser versión anime!")
        print(iText)
        option = int(input("Ingresa una opción: "))

        # to validate option input
        while not 0 < option < 4:
            option = int(input("Ingresa una opción válida: "))

        clean_terminal()

        # Opción qué es
        if option == 1:
            qText = dedent("""

            Eraser es un juego de mesa creado por el español Ignasi Ferré e ilustrado por Raúl Rojas.
            En este juego de 3 a 6 jugadores, tendrán que adivinar conceptos con pistas que
            desapareceran cada turno. Todos los jugadores tendrán que adivinar el mismo concepto dentro
            de 5 categorías (One piece - Naruto - Dragon ball - Spokon - Isekai) pero cada jugador tendrá
            una pista menos que el anterior.

            Este juego es una adaptación reducida y personalizada de Eraser original, lo cual reduce los conceptos
            y el tiempo de juego, pero comparte la misma esencia de los creadores originales.

            """)

            print(qText)
            input("Presiona Enter para continuar...")
            clean_terminal()

        # Opción instrucciones
        elif option == 2:
            insText = dedent(
                """

            -El jugador inicial deberá escoger una categoría y se le asignará un concepto,
            este debe escribir pistas de acuerdo a la cantidad de jugadores en la partida.
            -El siguiente jugador recibe una lista con las pistas del jugador al que se le
            asignó un concepto. Este debe intentar adivinar el concepto y escribirlo. Por
            último deberá eliminar una pista, lo cual el siguiente jugador recibe menos pistas.
            -El juego sigue la misma dinámica hasta que vuelve a ser el turno del jugador que
            recibe el concepto.

            """
            )
            eText = dedent(
                """

            Ejemplo de ronda:
            Una partida de 3 jugadores...
            -Turno jugador 1:
            El jugador 1 escoge la categoría One piece y recibe el concepto Luffy, este
            debe escribir 3 pistas y escribe [Sombrero, capitán, protagonista].
            -Turno jugador 2:
            El jugador 2 recibe las pistas [Sombrero, capitán, protagonista] y debe
            escribir el concepto que cree que tiene el jugador 1. Ahora debe escoger que
            pista eliminar y en este caso quiere eliminar [protagonista].
            -Turno jugador 3:
            El jugador 2 recibe las pistas [Sombrero, capitán] y debe escribir el
            concepto que cree que tiene el jugador 1.
            -Luego se revela el concepto y se asignan los puntajes correspondientes.

            """
            )

            pText = dedent(
                """

            Puntaje:
            Al jugador que recibe el concepto se le otorga 1 punto por cada persona que
            haya adivinado la palabra.
            Los jugadores que adivinaron el concepto reciben un punto.
            -----------------------------------------------------------------------------
                        Concepto   |   Puntaje    |    Palabra
            Jugador 1 : Luffy      |      1       |   ---------
            Jugador 2 : Luffy      |      1       |   Luffy
            Jugador 3 : Luffy      |      0       |   Buggy
            -----------------------------------------------------------------------------
                                          o
            -----------------------------------------------------------------------------
                        Concepto   |   Puntaje    |    Palabra
            Jugador 1 : Luffy      |      2       |   ---------
            Jugador 2 : Luffy      |      1       |   Luffy
            Jugador 3 : Luffy      |      1       |   Luffy
            -----------------------------------------------------------------------------

            """
            )

            print(insText)
            input("Presiona Enter para continuar...")
            print(eText)
            input("Presiona Enter para continuar...")
            print(pText)
            input("Presiona Enter para salir...")
            clean_terminal()


def score():
    pass


def game():
    pass


def clean_terminal():
    print("\n" * 50)


if __name__ == "__main__":
    main()
