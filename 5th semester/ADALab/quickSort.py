def quickSort(arr, low, high):
    if(low >= high):
        return arr
    pivot = low
    i = low + 1
    j = high + 1
    while(i < j):
        if arr[i] > arr[pivot]:
            arr[i], arr[j - 1] = arr[j - 1], arr[i]
            j -= 1
        else:
            i += 1
    arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
    pivot = i - 1
    quickSort(arr, low, pivot - 1)
    quickSort(arr, pivot + 1, high)

   
arr = list(map(int, input("Enter elements: ").split()))
quickSort(arr, 0, len(arr) - 1)
print("The sorted array is: ", end="")
for x in arr:
    print(x, end = " ")
   

   
            
