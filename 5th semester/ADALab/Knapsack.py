def knapsack(weights, values, capacity):
    n = len(weights)
    sack = [[0 for i in range(capacity + 1)] for j in range(n)]
    for i in range(n):
        for j in range(capacity + 1):
            if j - weights[i] >= 0:
                sack[i][j] = max(sack[i - 1][j], values[i] + sack[i - 1][j - weights[i]])
            else:
                sack[i][j] = sack[i - 1][j]
    return sack[n - 1][capacity]

weights = list(map(int, input("Enter weights").split()))
values = list(map(int, input("Enter values").split()))
capacity = int(input("Enter capacity"))
print(knapsack(weights, values, capacity))
