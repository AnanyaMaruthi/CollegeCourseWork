import random


def merge(arr, low, high, mid):
    comparisons = 0
    temp = [0 for i in range(low, high + 1)]
    i = low
    j = mid + 1
    k = 0
    while(i <= mid and j <= high):
        comparisons += 1
        if arr[i] <= arr[j]:
            
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1
    while(i <= mid):
        temp[k] = arr[i]
        k += 1
        i += 1
    while(j <= high):
        temp[k] = arr[j]
        k += 1
        j += 1
    k = 0
    for i in range(low, high + 1):
        arr[i] = temp[k]
        k += 1
    return comparisons


        
def mergeSort(arr, low, high):
    comparisons = 0
    if(low < high):
        mid = (low + high) // 2
        comparisons += mergeSort(arr, low, mid)
        comparisons += mergeSort(arr, mid + 1, high)
        comparisons += merge(arr, low, high, mid)
    return comparisons
        
        
def bubbleSort(arr):
    comparisons = 0;
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            comparisons += 1
            if(arr[j] > arr[j + 1]):
                
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return comparisons

def selectionSort(arr):
    comparisons = 0
    for i in range(len(arr) - 1):
        index = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if(arr[j] < arr[index]):               
                index = j
        arr[index], arr[i] = arr[i], arr[index]
    return comparisons
                
                
                
arr = [9,55,6,7,2,4,9,0,1,2,4,5,6,7,33,21,9,0,6]
n = int(input("Enter number of elements: "))
arr = [random.randint(0, 10000) for _ in range(n)]
arr1 = [arr[i] for i in range(n)]
arr2 = [arr[i] for i in range(n)]

comparisons = selectionSort(arr)
print("Number of comparisons in selection sort are", comparisons)


comparisons = bubbleSort(arr1)
print("Number of comparisons in bubble sort are", comparisons)

   

comparisons = mergeSort(arr, 0, len(arr) - 1)
print("Number of comparisons in merge sort are", comparisons)               
                
                
                
                
                
                
                
                
                
                
                
                
                

