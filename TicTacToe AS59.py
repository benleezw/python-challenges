board = [["*","*","*"],["*","*","*"],["*","*","*"]]
P1Win = False 
def printboard():
    print("  0 1 2")
    for i in range(3):
        print(i,*board[i])

def enterox(ox):
    Placed = False
    while Placed == False:
        x = int(input("input x position: "))
        while x > 2:
            x = int(input("input x position between 0 and 2: "))
        y = int(input("input y position: "))
        while y > 2:
            y = int(input("input y position between 0 and 2: "))
        if board[y][x] == "X" or board[y][x] == "Y":
            print("Spot already taken")
        else:
            board[y][x] = ox
            Placed = True

def playgame():
    printboard()
    won = False
    stalemate = False
    TurnPlayed = False

    while won is False or stalemate is False:
        if TurnPlayed is False:
            print()
            print("X's turn")
            ox = "X"
            TurnPlayed = True
        else:
            print()
            print("O's turn")
            ox = "O"
            TurnPlayed = False
        enterox(ox)
        print()
        printboard()

playgame()
