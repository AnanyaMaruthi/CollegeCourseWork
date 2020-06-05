player1 = "O" # Computer
player2 = "X" # Player
players = [player1, player2]

gameBoard = [["" for i in range(3)] for j in range(3)]
movesLeft = 9

# Maintain scores for each winnable line.
# +1 for "O". -1 for "X"
# 0 => line hasnt been played or isnt winnable
# 2 or -2 => the repective player has an impending win
rowScores = [0, 0, 0]
colScores = [0, 0, 0]
diagScores = [0, 0]

def displayBoard():
    for row in gameBoard:
        print(row)

def updateLineScores(player, row, col):
    if player == "O":
        lineScore = 1
    else:
        lineScore = -1
    rowScores[row] += lineScore
    colScores[col] += lineScore
    if row == col:
        diagScores[0] += lineScore
        if row == 1:
            diagScores[1] += lineScore
    if abs(row - col) == 2:
        diagScores[1] += lineScore


def makeMove(player, row, col):
    # Returns false if the cell is occupied, else makes the move and returns true 
    global gameBoard, movesLeft
    if gameBoard[row][col]:
        return False
    gameBoard[row][col] = player
    updateLineScores(player, row, col)
    movesLeft -= 1
    return True

def checkWin(row, col):
    # Returns (True, 1) if player 1 has won
    #         (True, -1) if player 2 has won
    #         (True, 0) if its a tie
    #         (False, 0) if the game is in progress
    winningScore = {player1 : 1, player2: -1}
    # Check row 
    if gameBoard[row][0] == gameBoard[row][1] == gameBoard[row][2]:
        return True, winningScore[gameBoard[row][col]]
    # Check column 
    if gameBoard[0][col] == gameBoard[1][col] == gameBoard[2][col]:
        return True, winningScore[gameBoard[row][col]]
    # Check major diagonal
    if row == col and gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2]:
        return True, winningScore[gameBoard[row][col]]
    # Check minor diagonal 
    if (abs(row - col) == 2 or row == col == 1) and gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0]:
        return True, winningScore[gameBoard[row][col]]
    # Tie 
    if movesLeft == 0:
        return True, 0
    # Game in progress 
    return False, 0

def checkProbableWin(player):
    if player == player1:
        checkScore = 2
    else:
        checkScore = -2
    # Check for a win in the major diagonal
    if diagScores[0] == checkScore:
        print("Major diag mmight win")
        for i in range(3):
            if gameBoard[i][i] == "":
                return (True, (i, i))

    # Check for a win in minor diagonal 
    if diagScores[1] == checkScore:
        print("Minor diag mmight win")
        if gameBoard[0][2] == "":
            return (True, (0, 2))
        if gameBoard[1][1] == "":
            return (True, (1, 1))
        if gameBoard[2][0] == "":
            return (True, (2, 0))
        

    # Check for a probable win in rows 
    for row in range(3):
        if rowScores[row] == checkScore:
            print("Row might win", row)
            for col in range(3):
                if gameBoard[row][col] == "":
                    return (True, (row, col))

    # Check for a probable win in columns 
    for col in range(3):
        if colScores[col] == checkScore:
            print("Col might win", col)
            for row in range(3):
                if gameBoard[row][col] == "":
                    return (True, (row, col))

    print("No probable win")
    return(False, ())

    
        

def getBestMove(prevRow, prevCol):
    # Returns (row, column)
    # If first move, return center cell
    if movesLeft == 9:
        return (1, 1)
    # If center is free, return center cell 
    if gameBoard[1][1] == "":
        return (1, 1)
    # If second move, return a corner
    if movesLeft == 8:
        return (0, 0)
    # Strategically return a corner
    # if movesLeft == 7:
    #     # Corner was not occupied by the opponent 
    #     if abs(prevRow - prevCol) == 1:
    #         if prevCol == 2:
    #             return (2, 0)
    #         if prevCol == 0:
    #             return (2, 2)
    #         if prevRow == 2:
    #             return (0, 0)
    #         if prevRow == 0:
    #             return (2, 2)
    #     else:
    #         # Occupy a corner in the same column
    #         if prevRow == 0:
    #             return (prevRow + 2, prevCol)
    #         elif prevRow == 2:
    #             return (0, prevCol)

    # Check if you have a probable win (Player 1) 
    probableWin, cell = checkProbableWin(player1)
    if probableWin:
        return cell 
    
    # Check if opponent has a probable win (Player 2)
    probableWin, cell = checkProbableWin(player2)
    if probableWin:
        return cell 

    # Return any free cell
    for row in range(3):
        for col in range(3):
            if gameBoard[row][col] == "":
                return (row, col)

    

def main():
    turn = 0
    row, col = -1, -1
    while True:
        player = players[turn]
        displayBoard()
        if turn == 1:
            row, col = list(map(int, input("Player " + str(turn + 1) + " : ").split()))
        else:
            print("My move")
            row, col = getBestMove(row, col)
        moveMade = makeMove(player, row, col)
        if moveMade == False:
            print("Invalid move")
            continue
        
        winStatus, score = checkWin(row, col)
        if winStatus:
            displayBoard()
            if score == 1:
                print("Player 1 wins")
            elif score == -1:
                print("Player 2 wins")
            else:
                print("Its a tie")
            break
        turn = (turn + 1) % 2

main()
