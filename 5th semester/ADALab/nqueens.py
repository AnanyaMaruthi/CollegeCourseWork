class Queen:
    def __init__(self, n):
        self.n = n
        self.column = [-1 for _ in range(n)]
        self.solution = 1
        
    def showBoard(self):
        print("SOLUTION:", self.solution, end="\n\n")
        self.solution += 1
        for i in range(self.n):
            print("0 " * self.column[i], 1, " 0" * (self.n - self.column[i] - 1), sep="")
        print()
            
    def place(self, k, i):
        for j in range(k):
            if self.column[j] == i or abs(self.column[j] - i) == abs(j - k):
                return False
        return True
                
        
    def nqueens(self, k):
        for i in range(self.n):
            if self.place(k, i):
                self.column[k] = i
                if k == self.n - 1:
                    self.showBoard()
                else:
                    self.nqueens(k + 1)
                
queen = Queen(int(input("Enter value of N")))
queen.nqueens(0)            
