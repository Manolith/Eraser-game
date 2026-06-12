import random
import time
from textwrap import dedent


def main():
    """
    1-one piece
    2-dragon ball
    3-naruto
    4-spokon
    5-isekai
    """

    concepts = {
        "es": {
            1: [
                "Luffy",
                "Zoro",
                "Nami",
                "Usopp",
                "Sanji",
                "Chopper",
                "Robin",
                "Franky",
                "Brook",
                "Jinbe",
                "Shanks",
                "Ace",
                "Sabo",
                "Barbanegra",
                "Law",
                "Kid",
                "Mihawk",
                "Buggy",
                "Akainu",
                "Kaido",
                "Big Mom",
                "Fruta del Diablo",
                "Haki",
                "Grand Line",
                "One Piece",
                "Going Merry",
                "Thousand Sunny",
                "Marina",
                "Yonko",
                "Sombrero de Paja",
            ],
            2: [
                "Goku",
                "Vegeta",
                "Gohan",
                "Trunks",
                "Piccolo",
                "Krillin",
                "Bulma",
                "Freezer",
                "Cell",
                "Majin Buu",
                "Beerus",
                "Whis",
                "Broly",
                "Jiren",
                "Yamcha",
                "Tenshinhan",
                "Maestro Roshi",
                "Shenlong",
                "Esferas del Dragon",
                "Kamehameha",
                "Genkidama",
                "Super Saiyajin",
                "Fusion",
                "Capsula Corp",
                "Torneo de Poder",
                "Nube Voladora",
                "Saiyajin",
                "Namekusei",
                "Radar del Dragon",
                "Habitacion del Tiempo",
            ],
            3: [
                "Naruto",
                "Sasuke",
                "Sakura",
                "Kakashi",
                "Jiraiya",
                "Tsunade",
                "Orochimaru",
                "Itachi",
                "Gaara",
                "Hinata",
                "Shikamaru",
                "Rock Lee",
                "Neji",
                "Madara",
                "Obito",
                "Pain",
                "Minato",
                "Kurama",
                "Hokage",
                "Sharingan",
                "Rinnegan",
                "Rasengan",
                "Chidori",
                "Akatsuki",
                "Aldea de la Hoja",
                "Examen Chunin",
                "Bijuu",
                "Chakra",
                "Jutsu",
                "Sello de Invocacion",
            ],
            4: [
                "Haikyuu",
                "Hinata Shoyo",
                "Kageyama Tobio",
                "Karasuno",
                "Nekoma",
                "Slam Dunk",
                "Hanamichi Sakuragi",
                "Rukawa",
                "Shohoku",
                "Kuroko no Basket",
                "Kuroko Tetsuya",
                "Kagami Taiga",
                "Generacion de los Milagros",
                "Blue Lock",
                "Isagi Yoichi",
                "Bachira Meguru",
                "Capitan",
                "Entrenador",
                "Torneo nacional",
                "Campeonato",
                "Partido",
                "Equipo",
                "Rival",
                "Victoria",
                "Derrota",
                "Voleibol",
                "Baloncesto",
                "Futbol",
                "Entrenamiento",
                "Trabajo en equipo",
            ],
            5: [
                "Reencarnacion",
                "Mundo paralelo",
                "Invocacion de heroe",
                "Rey Demonio",
                "Aventurero",
                "Gremio",
                "Mazmorra",
                "Nivel",
                "Experiencia",
                "Habilidad unica",
                "Magia",
                "Espadachin",
                "Sanador",
                "Arquero",
                "Bestia magica",
                "Elfo",
                "Enano",
                "Dragon",
                "Reino",
                "Princesa",
                "Demonio",
                "Espiritu",
                "Objeto legendario",
                "Jefe final",
                "Mision",
                "Inventario",
                "Teletransporte",
                "Sobrepotenciado",
                "Clase secreta",
                "Nivel maximo",
            ],
            6: [
                "Ingrese la cantidad de jugadores: ",
                "Ingrese los nombres de los jugadores: ",
                "Ingrese la cantidad de rondas a jugar:",
                "Turno de ",
                "Escoge una categoría",
                "Escribe tu pista: ",
                "Pistas",
                "Ingresa tu respuesta: ",
                "Esta es tu palabra: ",
                "Siguiente turno para adivinar comienza en...",
                "Siguiente turno para escribir pistas comienza en...",
                "Ingresa el número de la pista que deseas eliminar: ",
                "Tu pista no puede ser igual al concepto.",
            ],
            # Lista para validar datos
            7: [
                "Ingresa un valor correcto",
                "El jugador ",
                "tiene ",
                "puntos.",
                "punto.",
                "El ganador es ",
                "con",
                "¡Hay empate!",
                "El ",
                "ganador es ",
                "primer ",
                "segundo ",
                "tercer ",
            ],
        },
        "en": {
            1: [
                "Luffy",
                "Zoro",
                "Nami",
                "Usopp",
                "Sanji",
                "Chopper",
                "Robin",
                "Franky",
                "Brook",
                "Jinbe",
                "Shanks",
                "Ace",
                "Sabo",
                "Blackbeard",
                "Law",
                "Kid",
                "Mihawk",
                "Buggy",
                "Akainu",
                "Kaido",
                "Big Mom",
                "Devil Fruit",
                "Haki",
                "Grand Line",
                "One Piece",
                "Going Merry",
                "Thousand Sunny",
                "Marines",
                "Emperor",
                "Straw Hat",
            ],
            2: [
                "Goku",
                "Vegeta",
                "Gohan",
                "Trunks",
                "Piccolo",
                "Krillin",
                "Bulma",
                "Frieza",
                "Cell",
                "Majin Buu",
                "Beerus",
                "Whis",
                "Broly",
                "Jiren",
                "Yamcha",
                "Tien Shinhan",
                "Master Roshi",
                "Shenron",
                "Dragon Balls",
                "Kamehameha",
                "Spirit Bomb",
                "Super Saiyan",
                "Fusion",
                "Capsule Corp",
                "Tournament of Power",
                "Flying Nimbus",
                "Saiyan",
                "Namek",
                "Dragon Radar",
                "Hyperbolic Time Chamber",
            ],
            3: [
                "Naruto",
                "Sasuke",
                "Sakura",
                "Kakashi",
                "Jiraiya",
                "Tsunade",
                "Orochimaru",
                "Itachi",
                "Gaara",
                "Hinata",
                "Shikamaru",
                "Rock Lee",
                "Neji",
                "Madara",
                "Obito",
                "Pain",
                "Minato",
                "Kurama",
                "Hokage",
                "Sharingan",
                "Rinnegan",
                "Rasengan",
                "Chidori",
                "Akatsuki",
                "Hidden Leaf Village",
                "Chunin Exam",
                "Tailed Beast",
                "Chakra",
                "Jutsu",
                "Summoning Technique",
            ],
            4: [
                "Haikyuu",
                "Shoyo Hinata",
                "Tobio Kageyama",
                "Karasuno",
                "Nekoma",
                "Slam Dunk",
                "Hanamichi Sakuragi",
                "Rukawa",
                "Shohoku",
                "Kuroko no Basket",
                "Tetsuya Kuroko",
                "Taiga Kagami",
                "Generation of Miracles",
                "Blue Lock",
                "Yoichi Isagi",
                "Meguru Bachira",
                "Captain",
                "Coach",
                "National Tournament",
                "Championship",
                "Match",
                "Team",
                "Rival",
                "Victory",
                "Defeat",
                "Volleyball",
                "Basketball",
                "Soccer",
                "Training",
                "Teamwork",
            ],
            5: [
                "Reincarnation",
                "Parallel World",
                "Hero Summoning",
                "Demon King",
                "Adventurer",
                "Guild",
                "Dungeon",
                "Level",
                "Experience",
                "Unique Skill",
                "Magic",
                "Swordsman",
                "Healer",
                "Archer",
                "Magic Beast",
                "Elf",
                "Dwarf",
                "Dragon",
                "Kingdom",
                "Princess",
                "Demon",
                "Spirit",
                "Legendary Item",
                "Final Boss",
                "Quest",
                "Inventory",
                "Teleportation",
                "Overpowered",
                "Hidden Class",
                "Max Level",
            ],
            6: [
                "Enter the number of players: ",
                "Enter the players names: ",
                "Enter the number of rounds to play: ",
                "'s turn",
                "Choose a category",
                "Enter your clue: ",
                "Clues",
                "Enter your guess: ",
                "Your assigned concept is: ",
                "Next turn to guess starts in...",
                "Next turn to enter clues starts in...",
                "Enter the number of the clue you want to remove: ",
                "Your clue cannot be the same as the concept.",
            ],
            7: [
                "Enter a valid value",
                "Player ",
                "has ",
                "points.",
                "point.",
                "The winner is ",
                "with ",
                "It's a tie!",
                "The ",
                "winner is ",
                "first ",
                "second ",
                "third ",
            ],
        },
    }

    language = int(input("Welcome!\nSelect a language\n1-English\n2-Spanish\n"))
    clean_terminal()
    while not 0 < language < 3:
        language = int(input("Select a valid language\n1-English\n2-Spanish\n"))
        clean_terminal()

    if language == 1:
        instructions_en()
        game(concepts, "en")
    else:
        instructions_es()
        game(concepts, "es")


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

            Example Round:

            A 3-player game...

            -Player 1's turn:
            Player 1 chooses the One Piece category and is assigned the concept "Luffy".
            They must write 3 clues and choose: [Hat, Captain, Protagonist]

            -Player 2's turn:
            Player 2 receives the clues:
            [Hat, Captain, Protagonist]

            They must write down the concept they believe Player 1 was assigned. Then, they must choose one clue to remove.
            In this case, they decide to remove: [Protagonist]

            -Player 3's turn:
            Player 3 receives the clues: [Hat, Captain]
            They must write down the concept they believe Player 1 was assigned.

            -End of the round:
            The concept is revealed, and the corresponding points are awarded.

            """
            )
            pText = dedent(
                """

            Scoring:

            The player who was assigned the concept receives 1 point for each player who correctly guesses the word.
            Players who correctly guess the concept receive 1 point each.
            -----------------------------------------------------------------------------
                        Concept    |   Guess      |    Score
            Player  1 : Luffy      |  ---------   |      1
            Player  2 :   ?        |    Luffy     |      1
            Player  3 :   ?        |    Buggy     |      0
            -----------------------------------------------------------------------------
                                          or
            -----------------------------------------------------------------------------
                        Concept    |   Guess      |    Score
            Player  1 : Luffy      |  ---------   |      2
            Player  2 :   ?        |    Luffy     |      1
            Player  3 :   ?        |    Luffy     |      1
            -----------------------------------------------------------------------------

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
            El jugador 3 recibe las pistas [Sombrero, capitán] y debe escribir el
            concepto que cree que tiene el jugador 1.

            -Final de la ronda:
            Se revela el concepto y se asignan los puntajes correspondientes.

            """
            )

            pText = dedent(
                """

            Puntaje:
            Al jugador que recibe el concepto se le otorga 1 punto por cada persona que
            haya adivinado la palabra.
            Los jugadores que adivinaron el concepto reciben un punto.
            -----------------------------------------------------------------------------
                        Concepto   |   Palabra    |    Puntaje
            Jugador 1 : Luffy      |  ---------   |       1
            Jugador 2 :   ?        |    Luffy     |       1
            Jugador 3 :   ?        |    Buggy     |       0
            -----------------------------------------------------------------------------
                                          o
            -----------------------------------------------------------------------------
                        Concepto   |   Palabra    |    Puntaje
            Jugador 1 : Luffy      |  ---------   |       2
            Jugador 2 :   ?        |    Luffy     |       1
            Jugador 3 :   ?        |    Luffy     |       1
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


def game(concepts, lang):

    # setup game
    while True:
        try:
            cPlayers = int(input(f"{concepts[lang][6][0]} "))
            if 3 <= cPlayers <= 6:
                break
        except ValueError:
            print(f"{concepts[lang][7][0]}")

    players = []
    for i in range(cPlayers):
        player = input(f"{concepts[lang][6][1]} ")
        players.append(player)

    while True:
        try:
            cRounds = int(input(f"{concepts[lang][6][2]} "))
            break
        except ValueError:
            print(f"{concepts[lang][7][0]}")

    clean_terminal()
    # dictionary to alojate points
    dPlayers = {}
    for player in players:
        dPlayers[player] = 0
    # Create category lists
    op_list = concepts[lang][1]
    db_list = concepts[lang][2]
    na_list = concepts[lang][3]
    sp_list = concepts[lang][4]
    is_list = concepts[lang][5]
    # shuffle lists player's turn
    random.shuffle(players)
    # Variable to know the positions of players
    turn = 0
    lastPlayer = players[-1]
    for player in players:
        if lang == "es":
            print(f"{concepts[lang][6][3]}{player}\n")
        else:
            print(f"{player}{concepts[lang][6][3]}\n")

        # The player who gives the clues
        clues, guess = start_player(
            concepts,
            lang,
            cPlayers,
            players,
            cRounds,
            op_list,
            db_list,
            na_list,
            sp_list,
            is_list,
        )
        dPlayers = other_players(concepts, lang, clues, guess, players, turn, dPlayers)
        turn += 1
        clean_terminal()
        if player != lastPlayer:
            for key, value in dPlayers.items():
                if value > 1 or value < 1:
                    points = concepts[lang][7][3]
                else:
                    points = concepts[lang][7][4]

                print(
                    f"{concepts[lang][7][1]}{key} {concepts[lang][7][2]}{value} {points}"
                )
            time.sleep(5)
            clean_terminal()
            next_playerC(concepts, lang)
        clean_terminal()
    pWinnerl = []
    for key, value in dPlayers.items():
        if value > 1 or value < 1:
            points = concepts[lang][7][3]
        else:
            points = concepts[lang][7][4]

        print(f"{concepts[lang][7][1]}{key} {concepts[lang][7][2]}{value} {points}")

    winner = max(dPlayers.values())
    for key, value in dPlayers.items():
        if value == winner:
            pWinnerl.append(key)

    if len(pWinnerl) > 1:
        print(f"\n\n{concepts[lang][7][7]}")
        for pl in range(len(pWinnerl)):
            if pl == 0:
                print(
                    f"\n\n{concepts[lang][7][8]}{concepts[lang][7][10]}{concepts[lang][7][9]}{pWinnerl[pl]}"
                )
            elif pl == 1:
                print(
                    f"\n{concepts[lang][7][8]}{concepts[lang][7][11]}{concepts[lang][7][9]}{pWinnerl[pl]}"
                )

            else:
                print(
                    f"\n{concepts[lang][7][8]}{concepts[lang][7][12]}{concepts[lang][7][9]}{pWinnerl[pl]}"
                )

    else:
        pWinner = pWinnerl[0]
        print(
            f"\n\n{concepts[lang][7][5]}{pWinner} {concepts[lang][7][6]} {dPlayers[pWinner]} {concepts[lang][7][3]}"
        )


def start_player(
    concepts,
    lang,
    cPlayers,
    players,
    cRoounds,
    op_list,
    db_list,
    na_list,
    sp_list,
    is_list,
):
    while True:
        try:
            category = int(
                input(
                    f"{concepts[lang][6][4]}:\n \n1-One Piece\n2-Dragon Ball\n3-Naruto\n4-Spokon\n5-Isekai\n"
                )
            )

            if 1 <= category <= 5:
                break
            print(f"{concepts[lang][7][0]}")
        except ValueError:
            print(f"{concepts[lang][7][0]}")

    clean_terminal()
    list = concepts[lang][category]
    for r in range(10):
        random.shuffle(list)

    # print(list)
    guess = list.pop()
    print(f"{concepts[lang][6][8]}{guess}")
    # print(list)
    # Create list of clues
    clues = []
    for c in range(cPlayers):
        while True:
            try:
                clue = input(f"{concepts[lang][6][5]}\n")
                if clue.lower() != guess.lower():
                    break
            except ValueError:
                print(f"{concepts[lang][6][12]}")

        clues.append(clue)

    clean_terminal()

    return clues, guess


def other_players(concepts, lang, clues, guess, players, turn, dPlayers):
    # Change start_player position to skip
    lPlayers = players.copy()
    noGuesser = lPlayers.pop(turn)
    lastGuesser = lPlayers.pop(turn - 1)
    lPlayers.append(lastGuesser)
    lPlayers.append(noGuesser)

    # Guessing turns
    for i in range(len(lPlayers) - 1):
        if lang == "es":
            print(f"{concepts[lang][6][3]}{lPlayers[i]}\n")
        else:
            print(f"{lPlayers[i]}{concepts[lang][6][3]}\n")

        time.sleep(1)

        print(f"\n{concepts[lang][6][6]}\n")
        nClue = 1
        for clue in clues:
            print(f"{nClue}-{clue}")
            nClue += 1

        pGuess = input(f"\n{concepts[lang][6][7]}")

        while True:
            try:
                eClue = int(input(f"{concepts[lang][6][11]}"))
                if 1 <= eClue <= len(clues):
                    break
                print(f"{concepts[lang][7][0]}")
            except ValueError:
                print(f"{concepts[lang][7][0]}")

        clues.pop(eClue - 1)
        if pGuess.lower() == guess.lower():
            dPlayers[lPlayers[i]] += 1
            dPlayers[noGuesser] += 1

        clean_terminal()

        # End turn
        check = 2
        if (check + i) != len(players):
            next_player(concepts, lang)
            clean_terminal()

    return dPlayers


def next_player(concepts, lang):
    print(f"{concepts[lang][6][9]}")
    for i in range(5, -1, -1):
        print(i)
        time.sleep(1)


def next_playerC(concepts, lang):
    print(f"{concepts[lang][6][10]}")
    for i in range(5, -1, -1):
        print(i)
        time.sleep(1)


def clean_terminal():
    print("\n" * 50)


if __name__ == "__main__":
    main()
