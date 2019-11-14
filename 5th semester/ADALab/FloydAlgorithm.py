import sys

def floyd(matrix):
    n = len(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    print("Shortest distances is:")
    for i in range(n):
        print(matrix[i])

inf = sys.maxsize
matrix = [
    [0, 2, inf, 1, 8],
    [6, 0, 3, 2, inf],
    [inf, inf, 0, 4, inf],
    [inf, inf, 2, 0, 3],
    [3, inf, inf, inf, 0]
]
floyd(matrix)