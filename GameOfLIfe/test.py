import random
#https://stackoverflow.com/questions/18817207/use-python-to-create-2d-coordinate help with coming with how to assign coordinates

int = random.randrange(0,50)
board = []

def createBoard():
    global board
    for i in range(int):
        board.append([])
        for j in range(int):
            board[i].append(0)
    return board

def printBoard():
    global board
    for i in range(int):
        print(board[i])
    return board

def createPattern():
    global pattern
    global board
    global int
    boardindexlist = []
    for i in range(int):
        for j in range(int):
            boardindexlist.append([i, j])
    pattern = random.sample(boardindexlist, 4)
    print(pattern)
    return pattern

def addPattern():
    global board
    global int
    global pattern
    board[pattern[0][1]][pattern[0][0]] = 1
    board[pattern[1][1]][pattern[1][0]] = 1
    board[pattern[2][1]][pattern[2][0]] = 1
    board[pattern[3][1]][pattern[3][0]] = 1
    print("\t")
    for i in range(int):
        print(board[i])
    return board

class board:
    boards = createBoard()
    print = printBoard()
    createPat = createPattern()
    added = addPattern()


import random
class board:
    # creating the blank board
    int = random.randrange(0,50)
    board = []
    for i in range(int):
        board.append([])
        for j in range(int):
            board[i].append(0)
    for i in range(int):
        print(board[i])

    # creating a random pattern
    print("\t")
    boardindexlist = []
    for i in range(int):
        for j in range(int):
            boardindexlist.append([i, j])
    pattern = random.sample(boardindexlist,4)
    print(pattern)

    # printing pattern in grid
    board[pattern[0][1]][pattern[0][0]] = 1
    board[pattern[1][1]][pattern[1][0]] = 1
    board[pattern[2][1]][pattern[2][0]] = 1
    board[pattern[3][1]][pattern[3][0]] = 1


    for i in range(int):
        print(board[i])
