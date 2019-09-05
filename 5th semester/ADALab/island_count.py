def isSafe(i, j, N, M):
    if (i >= 0 and i < N and j >= 0 and j < M):
        return True
    return False
        

def searchIsland(i, j, matrix):
    N = len(matrix)
    M = len(matrix[0])
    matrix[i][j] = 0
    if(isSafe(i - 1, j, N, M) and matrix[i - 1][j] == 1):
        searchIsland(i - 1, j, matrix)
    if(isSafe(i + 1, j, N, M) and matrix[i + 1][j] == 1):
        searchIsland(i + 1, j, matrix)
    if(isSafe(i, j - 1, N, M) and matrix[i][j - 1] == 1):
        searchIsland(i, j - 1, matrix)
    if(isSafe(i, j + 1, N, M) and matrix[i][j + 1] == 1):
        searchIsland(i, j + 1, matrix)
    if(isSafe(i - 1, j - 1, N, M) and matrix[i - 1][j - 1] == 1):
        searchIsland(i - 1, j - 1, matrix)
    if(isSafe(i - 1, j + 1, N, M) and matrix[i - 1][j + 1] == 1):
        searchIsland(i - 1, j + 1, matrix)
    if(isSafe(i + 1, j - 1, N, M) and matrix[i + 1][j - 1] == 1):
        searchIsland(i + 1, j - 1, matrix)
    if(isSafe(i + 1, j + 1, N, M) and matrix[i + 1][j + 1] == 1):
        searchIsland(i + 1, j + 1, matrix)
        
def countIslands(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                count += 1
                searchIsland(i, j, matrix)
    return count

rows = int(input("Enter number of rows: "))
matrix = []
for i in range(rows):
    matrix.append(list(map(int, input("Enter row").split())))
count = countIslands(matrix)
print("The number of islands are", count)
