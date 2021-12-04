file = open("4\\input.txt", "r")
numbers = file.readline().split("\n")[0].split(",")
boardsNumbers = file.read().split()

class Field:
    def __init__(self, number):
        self.marked = False
        self.number = number

class Board:
    def __init__(self, array, numberOfBoards):
        self.win = False
        self.grid = [[0 for i in range(5)] for j in range(5)]
        self.createGrid(array, numberOfBoards)
        self.lastNumber = -1
        self.rank = 0
        self.sum = 0

    
    def createGrid(self, array, numberOfBoards):
        for i in range(5):
            for j in range(5):
                self.grid[i][j] = Field(int(array[numberOfBoards*25 + i*5 + j]))

    def __str__(self):
        string = ""
        for i in range(5):
            for j in range(5):
               string += str(self.grid[i][j].number) + " "
            string += "\n"
        return string
    
    def markNumber(self, number):
        for i in range(5):
            for j in range(5):
                if(self.grid[i][j].number == number):
                    self.grid[i][j].marked = True

    def checkWin(self):
        row = 0
        column = 0
        for i in range(5):
            for j in range(5):
                if(self.grid[i][j].marked == True):
                    row += 1
                if(self.grid[j][i].marked == True):
                    column += 1
            if(row == 5 or column == 5):
               self.win = True
               self.rank = rank
            else:
                row = 0
                column = 0

    def calculateUnMarked(self):
        for i in range(5):
            for j in range(5):
                if(self.grid[i][j].marked == False):
                    self.sum += self.grid[i][j].number

    def setLastNumber(self, number):
        self.lastNumber = number
        
    def setRank(self, rank):
        self.rank = rank



i = 0
boards = []
while(i != int(len(boardsNumbers)/25)):
    boards.append(Board(boardsNumbers, i))
    i += 1

rank = 0
for i in range(len(numbers)):
    for j in range(len(boards)):
        if(boards[j].win != True):
            boards[j].markNumber(int(numbers[i]))
            boards[j].checkWin()
            if(boards[j].win):
                rank += 1
                boards[j].setRank(rank)
                boards[j].setLastNumber(int(numbers[i]))
                boards[j].calculateUnMarked()

last = -1
first = -1
for i in range(len(boards)):
    if(boards[i].rank == (rank)): #part2
        last = i
    if(boards[i].rank == 1): #part1
        first = i

#part1
print("winning board: score is: ", boards[first].sum*boards[first].lastNumber)
#part2
print("last winning board: score is: ", boards[last].sum*boards[last].lastNumber)


