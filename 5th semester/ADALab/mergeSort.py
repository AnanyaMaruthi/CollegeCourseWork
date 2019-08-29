def merge(arr, low, high, mid):
    temp = [0 for i in range(low, high + 1)]
    i = low
    j = mid + 1
    k = 0
    while(i <= mid and j <= high):
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


        
def mergeSort(arr, low, high):
    if(low < high):
        mid = (low + high) // 2
        mergeSort(arr, low, mid)
        mergeSort(arr, mid + 1, high)
        merge(arr, low, high, mid)

    
    
arr = list(map(int, input("Enter elements: ").split()))
mergeSort(arr, 0, len(arr) - 1)
print("The sorted array is: ", end="")
for x in arr:
    print(x, end = " ")
