# Using DFS/BFS, Given a 2D matrix of 0s and 1s, find total number of clusters or islands formed by elements with value 1
class Island:
    def __init__(self):
        self.matrix = []
        self.rows, self.columns = map(int, input("Enter number of rows and columns").split())
        for i in range(self.rows):
            print("Enter row", i + 1)
            row = list(map(int, input().split()))
            self.matrix.append(row)

    def isValid(self, row, column):
        if row >= 0 and row < self.rows and column >= 0 and column < self.columns:
            return True
        return False

    def traverseIsland(self, row, col):
        row_helper = [-1, -1, -1, 0, 0, 1, 1, 1]
        col_helper = [-1, 0, 1, -1, 1, -1, 0, 1]
        # Check all neighbours
        for i in range(8):
            if self.isValid(row + row_helper[i], col + col_helper[i]):
                if self.matrix[row + row_helper[i]][col + col_helper[i]] == 1:
                    self.matrix[row + row_helper[i]][col + col_helper[i]] = 0
                    self.traverseIsland(row + row_helper[i], col + col_helper[i])

    def countIslands(self):
        islands = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.matrix[i][j] == 1:
                    self.matrix[i][j] = 0
                    islands += 1
                    self.traverseIsland(i, j)
        return islands

island = Island()
print(island.countIslands())
