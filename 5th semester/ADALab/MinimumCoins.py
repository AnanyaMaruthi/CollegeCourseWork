def getMinCoinsDP(amount, denominations, index, table):
    # print(amount, index)
    if amount == 0:
        table[index][amount] = 0
        return table[index][amount]

    if denominations[index] == 1: #This condition must occur
        table[index][amount] = amount
        return table[index][amount]

    if table[index][amount] != -1:
        return table[index][amount]

    if denominations[index] > amount:
        table[index][amount] = getMinCoinsDP(amount, denominations, index - 1, table)

    else:
        coins = amount // denominations[index]
        amount = amount % denominations[index]
        # print(coins, amount)
        table[index][amount] = coins + getMinCoinsDP(amount, denominations, index - 1, table)

    return table[index][amount]
    
    

amount = int(input("Enter the amount"))
denominations = list(map(int, input("Enter the denominations").split()))
table = [[-1 for col in range(amount + 1)] for row in range(len(denominations))]
print("DP Soln:", getMinCoinsDP(amount, denominations, len(denominations) - 1, table))
getMinimumCoins(amount, denominations)
