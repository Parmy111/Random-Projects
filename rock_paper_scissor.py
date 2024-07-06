import random

options = ["rock", "paper", "scissor"]

player = None

gameRunning = True

def game():
    global gameRunning
    randomChoice = random.choice(options)
    player = input("Enter a choice ('rock', 'paper', or 'scissor'): ")
    print(f"You chose: {player}")
    print(f"The computer chose: {randomChoice}")
    if randomChoice == "rock" and player == "rock":
        print("Both of you chose rock, it ends in a tie!!! The game shall continue.")
    if randomChoice == "paper" and player == "paper":
        print("Both of you chose paper, it ends in a tie!!! The game shall continue.")
    if randomChoice == "scissor" and player == "scissor":
        print("Both of you chose rock, it ends in a tie!!! The game shall continue.")
    if randomChoice == "rock" and player == "paper":
        print("You Won!")
        gameRunning = False
    if randomChoice == "paper" and player == "scissor":
        print("You Won!")
        gameRunning = False
    if randomChoice == "scissor" and player == "rock":
        print("You Won!")
        gameRunning = False
    if player == "rock" and randomChoice == "paper":
        print("You Lost!")
        gameRunning = False
    if player == "paper" and randomChoice == "scissor":
        print("You Lost!")
        gameRunning = False
    if player == "scissor" and randomChoice == "rock":
        print("You Lost!")
        gameRunning = False
while gameRunning == True:
    game()