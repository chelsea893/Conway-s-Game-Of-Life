import random
#https://stackoverflow.com/questions/18817207/use-python-to-create-2d-coordinate help with coming with how to assign coordinates

int = random.randrange(1,50)
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
    for i in range(len(pattern)):
        board[pattern[i][0]][pattern[i][1]] = 1

    print("\t")
    for i in range(int):
        print(board[i])
    return board

class board:
    boards = createBoard()
    print = printBoard()
    createPat = createPattern()
    added = addPattern()