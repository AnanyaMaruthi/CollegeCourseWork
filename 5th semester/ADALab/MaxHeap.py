def leftChild(n):
    return 2 * n + 1

def rightChild(n):
    return 2 * n + 2

def isMaxHeap(array, index):
    if rightChild(index) >= len(array):
        if leftChild(index) >= len(array):
            return True
        else:
            if array[index] > array[leftChild(index)]:
                return True
            else:
                return False

    if (array[index] > array[leftChild(index)] and
       array[index] > array[rightChild(index)] and 
       isMaxHeap(array, leftChild(index)) and
       isMaxHeap(array, rightChild(index))):
       return True
    
    return False


array = list(map(int, input("Enter elements").split()))
# array = [90, 15, 10, 7, 12, 2] TRUE
# array = [9, 15, 10, 7, 12, 11] FALSE
print(isMaxHeap(array, 0))
