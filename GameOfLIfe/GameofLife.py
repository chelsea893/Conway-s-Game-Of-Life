import random
from copy import copy, deepcopy
class board:
    def __init__(self, row, col): # constructor
        self.board = []
        for i in range(row):
            self.board.append([])
            for j in range(col):
                self.board[i].append(0)
        self.printboard()

    def printboard(self):
        print("Print board")
        for list in self.board:
            print(list)

    def setPattern(self, ro, co):
        indexlist = []
        for i in range(0,ro):
            for j in range(0,co):
                indexlist.append([i,j])
        print(indexlist)
        self.pattern = random.sample(indexlist,30)
        print("Randomly chosen coordinates" + str(self.pattern))
        self.changepattern(self.pattern)

    def changepattern(self, index):
        print("index", index)
        for a,b in index:
            self.board[a][b] = 1
        self.printboard()
        self.rules()


    def rules(self):
        self.updateboard = deepcopy(self.board)
        itr = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                value = self.board[i][j]
                print("""
___________________________________________________________________________________________________________________________________________
                """)
                print("index value: " + str(value))
                if (value == 1):
                    direction = [[1, 1], [1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1]]
                    print("index: ")
                    print(i, j)
                    neighbours = []
                    row = i
                    column = j
                    for elem in direction:
                        row_inc, col_inc = elem[0], elem[1]
                        newR = row + row_inc
                        newR = int(newR)
                        newC = column + col_inc
                        newC = int(newC)
                        if (newR >= 0) and (newR < 10) and (newC >= 0) and (newC < 10):
                            print("neighbour index:", newR, newC)
                            print("index value: ")
                            print(self.board[newR][newC])
                            neighbours.append(self.board[newR][newC])
                    print(neighbours)
                    countAlive = neighbours.count(1)
                    countDead = neighbours.count(0)
                    if countAlive == 2 or countAlive == 3:
                        self.updateboard[i][j] = 1
                        print("true")
                    else:
                        self.updateboard[i][j] = 0
                    print("alive: " + str(countAlive))
                    print("dead: " + str(countDead))
                if (value == 0):
                    direction = [[1, 1], [1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1]]
                    print("index: ")
                    print(i, j)
                    neighbours = []
                    row = i
                    column = j
                    for elem in direction:
                        row_inc, col_inc = elem[0], elem[1]
                        newR = row + row_inc
                        newR = int(newR)
                        newC = column + col_inc
                        newC = int(newC)
                        if (newR >= 0) and (newR < 10) and (newC >= 0) and (newC < 10):
                            print("neighbour index:", newR, newC)
                            print("index value: ")
                            print(self.board[newR][newC])
                            neighbours.append(self.board[newR][newC])
                    print(neighbours)

                    countAlive = neighbours.count(1)
                    countDead = neighbours.count(0)
                    if countAlive == 3:
                        self.updateboard[i][j] = 1
                        print("true")
                    else:
                        self.updateboard[i][j] = 0
                    print("alive: " + str(countAlive))
                    print("dead: " + str(countDead))
        for list in self.updateboard:
            print(list)
        self.board = self.updateboard



if __name__ == "__main__":
    row = 10
    column = 10
    board_ = board(row, column)
    print("Moving to set pattern")
    board_.setPattern(row, column)

