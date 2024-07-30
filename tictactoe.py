def printBoard(xState, zState):
    board = []
    for i in range(9):
        if xState[i]:
            board.append('X')
        elif zState[i]:
            board.append('O')
        else:
            board.append(str(i))
    
    print(f"{board[0]} | {board[1]} | {board[2]} ")
    print("--|---|---")
    print(f"{board[3]} | {board[4]} | {board[5]} ")
    print("--|---|---")
    print(f"{board[6]} | {board[7]} | {board[8]} ")

def checkWin(xState, zState):
    xwins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for win in xwins:
        if xState[win[0]] and xState[win[1]] and xState[win[2]]:
            print("X Won the match")
            return 1
        if zState[win[0]] and zState[win[1]] and zState[win[2]]:
            print("O Won the match")
            return 1
    return 0

if __name__ == "__main__":
    xState = [0] * 9
    zState = [0] * 9
    turn = 1
    print("Welcome to Tic Tac Toe")

    while True:
        printBoard(xState, zState)
        
        if turn == 1:
            print("X's chance")
        else:
            print("O's chance")
        
        while True:
            try:
                value = int(input("Please enter a value (0-8): "))
                if value < 0 or value > 8:
                    print("Invalid input. Please enter a number between 0 and 8.")
                elif xState[value] or zState[value]:
                    print("Position already taken. Choose another.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 8.")

        if turn == 1:
            zState[value] = 1
        else:
            xState[value] = 1

        if checkWin(xState, zState):
            break
        
        turn = 1 - turn
