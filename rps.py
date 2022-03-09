#Random Librery
import os
import getpass
import random

#Constants
equals = ("==============================================")
tittle = ('|-------------ROCK, PAPER, SCISSORS----------|')
shapes = ["r", "p", "s"]
clear = lambda: os.system('cls')

def whoWins(x, y):

    shape_x = x
    shape_y = y
    boolean = False

    if ((shape_x == "r" and shape_y == "s") or
        (shape_x == "s" and shape_y == "p") or
        (shape_x == "p" and shape_y == "r")):
            boolean = True
            return boolean

    return boolean

def rockPaperScissors(op):

    clear()

    wins_p1 = 0
    wins_p2 = 0
    boolean = True

    print(equals)
    print(tittle)
    print(f"{equals}\n\n")

    if op == 1:

        while (wins_p1 + wins_p2) != rounds:

            print(f"|--------------- Best of {rounds} -----------|")
            print(f"|--- {player1} Wins: {wins_p1} | {player2} Wins: {wins_p2} ---|\n")

            while boolean:
                shape_p1 = getpass.getpass(f"Please, choose a shape {player1} (r, p, s): ").lower()

                if shape_p1 in shapes:
                    print()
                    boolean = False 
                
                else:
                    print(f"\n|--- ERROR: {player1}, the shape entered is invalid ---|\n")

            boolean = True

            while boolean:
                shape_p2 = getpass.getpass(f"Please, choose a shape {player2} (r, p, s): ").lower()

                if shape_p2 in shapes:
                    print()
                    boolean = False 
                
                else:
                    print(f"\n|--- ERROR: {player2}, the shape entered is invalid ---|\n")

            boolean = True


            if shape_p1 == shape_p2:
                clear()
                print(equals)
                print("|------------------- DRAW ------------------|")
                print(f"|------- {player1} Shape: {shape_p1.upper()} | {player2} Shape: {shape_p2.upper()} ------|")
                print(equals)
                print()

            elif whoWins(shape_p1, shape_p2):
                wins_p1 += 1
                clear()
                print(equals)
                print(f"|---------------- {player1} Wins ----------------|")
                print(f"|------- {player1} Shape: {shape_p1.upper()} | {player2} Shape: {shape_p2.upper()} ------|")
                print(equals)
                print()
            
            else:
                wins_p2 += 1
                clear()
                print(equals)
                print(f"|---------------- {player2} Wins ----------------|")
                print(f"|------- {player1} Shape: {shape_p1.upper()} | {player2} Shape: {shape_p2.upper()} ------|")
                print(equals)
                print()

    else:

         while (wins_p1 + wins_p2) != rounds:

            print(f"|--------------- Best of {rounds} -----------|")
            print(f"|--- {player1} Wins: {wins_p1} | {player2} Wins: {wins_p2} ---|\n")
            
            while boolean:
                shape_p1 = getpass.getpass(f"Please, choose a shape {player1} (r, p, s): ").lower()

                if shape_p1 in shapes:
                    print()
                    boolean = False 
                
                else:
                    print(f"\n|--- ERROR: {player1}, the shape entered is invalid ---|\n")

            boolean = True
            
            shape_p2 = random.choice(shapes)


            if shape_p1 == shape_p2:
                clear()
                print(equals)
                print("|------------------- DRAW ------------------|")
                print(f"|------- {player1} Shape: {shape_p1.upper()} | {player2} Shape: {shape_p2.upper()} ------|")
                print(equals)
                print()

            elif whoWins(shape_p1, shape_p2):
                wins_p1 += 1
                clear()
                print(equals)
                print(f"|---------------- {player1} Wins ----------------|")
                print(f"|------- {player1} Shape: {shape_p1.upper()} | {player2} Shape: {shape_p2.upper()} ------|")
                print(equals)
                print()
            
            else:
                wins_p2 += 1
                clear()
                print(equals)
                print(f"|---------------- {player2} Wins ----------------|")
                print(f"|------- {player1} Shape: {shape_p1.upper()} | {player2} Shape: {shape_p2.upper()} ------|")
                print(equals)
                print()

    if wins_p1 > wins_p2:

        clear()
        print(f"|----------------- Best of {rounds} ----------------|")
        print(f"|------- {player1} Wins: {wins_p1} | {player2} Wins: {wins_p2} ------|\n")

        print(equals)
        print(f"|---------------- {player1} Wins ----------------|")
        print(equals)

    else:

        clear()
        print(f"|----------------- Best of {rounds} ----------------|")
        print(f"|------- {player1} Wins: {wins_p1} | {player2} Wins: {wins_p2} ------|\n")

        print(equals)
        print(f"|---------------- {player2} Wins ----------------|")
        print(equals)

    input('\nPress any key for continue...')
    main()

def menuGame(op):

    clear()

    global player1, player2, rounds
    boolean = True

    if op == 1:

        print(equals)
        print(tittle)
        print(f"{equals}\n\n")

        while boolean:
            rounds = int(input("Please, enter how many rounds you will play: "))

            if rounds % 2 == 1:
                boolean = False
                print()

            else:
                print("\n|--- ERROR: The number of rounds must be odd ---|\n")
            
            

        player1 = input("Please, enter player 1 name: ")
        print()
        player2 = input("Please, enter player 2 name: ")

        rockPaperScissors(1)

    elif op == 2:

        print(equals)
        print(tittle)
        print(f"{equals}\n\n")

        while boolean:
            rounds = int(input("Please, enter how many rounds you will play: "))

            if rounds % 2 == 1:
                boolean = False
                print()

            else:
                print("\n|--- ERROR: The number of rounds must be odd ---|\n")

        player1 = input("Please, enter player name: ")
        player2 = "IA"

        rockPaperScissors(2)

    elif op == 3:

        clear()

        print(equals)
        print("|------------------CONTROLS------------------|")
        print(f"{equals}\n\n")

        print("|--- For rock use 'r' ---|")
        print("|--- For paper use 'p' ---|")
        print("|--- For scissors use 's' ---|\n\n")

        print(equals)
        print("|------------------GOOD LUCK!----------------|")
        print(f"{equals}\n")

        input('Press any key to continue...')
        menu(1)

    elif op == 4:
        main()

def menu(op):
    
    if op == 1:
        
        clear()

        while True:
            print(equals)
            print(tittle)
            print(f"{equals}\n\n")

            try:
                print("1. Player vs Player")
                print("2. Player vs IA")
                print("3. Controls")
                print("4. Back")

                mode = int(input("\nPlease, choose a mode to continue: "))

                if mode < 1 or mode > 4:
                    print("\n|--- ERROR: The option entered is invalid ---|\n")

            except (ValueError, TypeError, IndexError):
                print("\n|--- ERROR: The data entered is invalid ---|\n")

            finally:
                menuGame(mode)

    elif op == 2:
        
        clear()

        print(equals)
        print("|-----------------INSTRUCCIONS---------------|")
        print(f"{equals}\n\n")

        print("Rock, paper, scissors is a hand game, usually played between two players,")
        print("in which each player simultaneously forms one of three shapes with an outstretched hand.")
        print("These shapes are 'rock', 'paper' or 'scissors'.")

        print("Then they must play a number of odd rounds, assigned by one of the players and the one with")
        print("the most rounds wins. Remember:\n")
        print("Rock beats Scissors\nScissors beats Paper\nPaper beats Rock\n\n")

        print(equals)
        print("|------------------GOOD LUCK!----------------|")
        print(f"{equals}\n")

        input('Press any key to continue...')
        menu(1)
        
    elif op == 3:
        
        clear()

        print("\n|---- Thanks for playing :D ---|\n\n")
        quit()

def main():
    clear()

    while True:  
          
        print(equals)
        print("|---- Welcome to 'Rock, Paper, Scissors' ----|")
        print(f"{equals}\n\n")

        try:
            print("1. Play")
            print("2. Instruccions")
            print("3. Exit")

            option = int(input("\nPlease choose a option to continue: "))

            if option < 1 or option > 3:
                print("\n|--- ERROR: The option entered is invalid ---|\n")

        except (ValueError, TypeError, IndexError):
            print("\n|--- ERROR: The data entered is invalid ---|\n")

        finally:
            menu(option)

main()