import random

board = ["-", "-", "-", 
         "-", "-", "-",
        "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True
#Create the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
#Take player input
def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >=1 and inp <=9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Someone already has that spot!")
        playerInput(board)
#check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[3]
        return True
def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != "-":
        winner = board[0]
        return True
    if board[1] == board[4] == board[7] and board[4] != "-":
        winner = board[1]
        return True
    if board[2] == board[5] == board[8] and board[5] != "-":
        winner = board[2]
        return True
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[4] != "-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[0]
        return True
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("IT ENDED IN A TIE D::::::::")
        gameRunning = False
    
#global keyword makes it so that a change within a function causes a change in the whole function

#switch sides
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
#check for win or tie again

def checkWin():
    global gameRunning
    if checkHorizontal(board) or checkDiagonal(board) or checkVertical(board):
        print(f"The winner is {winner}")
        gameRunning = False

#computer
def computer(board):
    while currentPlayer == "O":
        w = random.randint(0,8)
        if board[w] == "-":
            board[w] = "O"
            switchPlayer()

#Running the game
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)