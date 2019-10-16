class Queens:
    def __init__ (self, N):
        self.N = N
        self.yPositions = [-1 for _ in range(N)]
        self.solutions = 0

    def showBoard(self):
        print("SOLUTION:", self.solutions + 1)
        self.solutions += 1
        for i in self.yPositions:
            print( "0 " * i, "1 ", "0 " * (self.N - i - 1), sep="")

    def isSafe(self, row, col):
        for i in range(row):
            if col == self.yPositions[i]:
                return False
            if abs(row - i) == abs(col - self.yPositions[i]):
                return False
        return True
    
    def placeQueen(self, row):
        for col in range(self.N):
            if self.isSafe(row, col):
                self.yPositions[row] = col
                if row == self.N - 1:
                    self.showBoard()
                else:
                    self.placeQueen(row + 1)


queens = Queens(4)
queens.placeQueen(0)
