# Using backtracking, Solve Rat in Maze problem

def display(maze, path):
    for node in path:
        x, y = node 
        maze[x][y] = "*"
    for row in maze:
        for col in row:
            print(col, end = " ")
        print()

def solveMaze(maze, i, j, path=[]):
    if i < 0 or j < 0 or i >= len(maze) or j >= len(maze): 
        return False

    if  maze[i][j] == 0:
        return False

    if i == len(maze) - 1 and j == len(maze) - 1:
        path.append((i, j))
        display(maze, path)
        return True
    
    else:
        path.append((i, j))
        if solveMaze(maze, i + 1, j, path):
            return True
        elif solveMaze(maze, i, j + 1, path):
            return True
        print("Cant solve")
        return False

N = int(input("Enter N: "))
maze = []
print("Enter maze: ")
for i in range(N):
    row = list(map(int, input().split()))
    maze.append(row)
solveMaze(maze, 0, 0)