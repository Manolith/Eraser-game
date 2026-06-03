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
            print(2)


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
            print(2)
            input("Presiona Enter para continuar.")
            clean_terminal()


def score():
    pass


def game():
    pass


def clean_terminal():
    print("\n" * 50)


if __name__ == "__main__":
    main()
