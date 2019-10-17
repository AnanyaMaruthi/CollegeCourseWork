# Using Backtracking, solve Sum of Subsets problem
def display(subset):
    for element in subset:
        print(element, end=" ")
    print()

def sumofSubsets(set, sum, index, subset=[]):
    if index < 0:
        return 

    if set[index] == sum:
        subset1 = subset.copy()
        subset1.append(set[index])
        display(subset1)
        return sumofSubsets(set, sum, index - 1, subset)
    
    if set[index] > sum:
        return sumofSubsets(set, sum, index - 1, subset)
    
    sum1 = sum - set[index]
    subset1 = subset.copy()
    subset1.append(set[index])
    return sumofSubsets(set, sum1, index - 1, subset1) or sumofSubsets(set, sum, index - 1, subset)

inputSet = list(map(int, input("Enter the set").split()))
inputSum = int(input("Enter sum "))
sumofSubsets(inputSet, inputSum, len(inputSet) - 1)

