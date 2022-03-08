#Random Librery
import os

equals = ("=========================================")
clear = lambda: os.system('cls')

def rockPaperScissors(op):
    
    if op == 1:
        return
    elif op == 2:
        return

def menu(op):
    
    if op == 1:
        rockPaperScissors(x)
    elif op == 2:
        return
    elif op == 3:
        return

def main():
    clear()
    print(equals)
    print("|-----Welcome to 'Rock, Paper, Scissors'-----|")
    print(f"{equals}\n")

    print("1. Play")
    print("2. Instruccions")
    print("3. Exit")

    option = int(input("\nPlease choose a option to continue: "))
    
    menu(option)