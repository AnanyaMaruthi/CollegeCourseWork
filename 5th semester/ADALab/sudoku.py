class Sudoku:
    #int N
    
    def __init__(self, N):
        self.N = N
        self.grid = []
        
    def setProblem(self):
        for x in range(self.N):
            row = list(map(int, input().split()))
            self.grid.append(row)
            
    def isSafeRow(self, row, digit):
        for i in range(N):
            if self.grid[row][i] == digit:
                return False
        return True
        
    def isSafeColumn(self, column, digit):
        for i in range(N):
            if self.grid[i][column] == digit:
                return False
        return True
        
    def isSafeGrid(self, row, column, digit):
        gridSize = int(self.N ** 0.5)
        
        rowStart = (row // gridSize) * gridSize
        columnStart = (column // gridSize) * gridSize
        #print(row, column, gridSize, rowStart, columnStart)
        for i in range(rowStart, rowStart + gridSize):
            for j in range(columnStart, columnStart + gridSize):
                if self.grid[i][j] == digit:
                    return False
        return True
        
    def findUnassigned(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.grid[i][j] == 0:
                    return i, j
        return -1, -1
        
    def solve(self):
        row, column = self.findUnassigned()
        if row == -1:
            return True
        for digit in range(1, self.N + 1):
            if self.isSafeRow(row, digit) and self.isSafeColumn(column, digit) and self.isSafeGrid(row, column, digit):
                self.grid[row][column] = digit
                if(self.solve() == True):
                    return True
                else:
                    self.grid[row][column] = 0
        #self.grid[row][column] = 0
        return False
        
    def printGrid(self):
        for i in range(self.N):
            for j in range(self.N):
                print(self.grid[i][j], end=" ")
            print()
            
        
        
N = int(input("Enter grid size"))        
sudoku = Sudoku(N)
sudoku.grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
               [5, 2, 0, 0, 0, 0, 0, 0, 0],
               [0, 8, 7, 0, 0, 0, 0, 3, 1],
               [0, 0, 3, 0, 1, 0, 0, 8, 0],
               [9, 0, 0, 8, 6, 3, 0, 0, 5],
               [0, 5, 0, 0, 9, 0, 6, 0, 0],
               [1, 3, 0, 0, 0, 0, 2, 5, 0],
               [6, 9, 0, 3, 5, 0, 0, 0, 4],
               [7, 0, 5, 2, 8, 0,  0, 1, 9]]
sudoku.solve()
sudoku.printGrid()

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
