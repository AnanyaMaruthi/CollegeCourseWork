def drawLines(rows, columns):
    print("--" * columns)
    for i in range(rows):
        print(" |" * columns)
        print("--" * columns)

drawLines(3, 4)