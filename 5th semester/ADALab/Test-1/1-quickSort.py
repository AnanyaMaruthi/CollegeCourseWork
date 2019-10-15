# Using Quick Sort, Given an array of n numbers, the task is to answer the following queries:
# Kth Smallest(start, end, k) : Find the Kth smallest number in the range from array index 'start' to 'end'.

def partition(array, low, high):
    key = array[low]
    i = low + 1
    j = high
    while(i < j):
        if array[i] < key:
            i += 1
        elif array[i] > key:
            array[i], array[j] = array[j], array[i]
            j -= 1
    array[low], array[i] = array[i], array[low]
    return i

def kSmallest(array, start, end, k):
    if start == end:
        if start == k:
            return array[k]
        else:
            return -1
    partitionIndex = partition(array, start, end)
    if k == partitionIndex:
        return array[k]
    elif k < partitionIndex:
        return kSmallest(array, start, partitionIndex - 1, k)
    else:
        return kSmallest(array, partitionIndex + 1, end, k)
        
def util(array, start, end, k):
    start -= 1
    end -= 1
    k += start - 1
    return kSmallest(array, start, end, k)

array = [3, 2, 5, 1, 8, 9]
start = 1
end = 6
k = 4
print(util(array, start, end, k))
