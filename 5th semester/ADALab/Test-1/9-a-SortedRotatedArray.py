# Search an element in a sorted and rotated array

def Search(array, element, low, high):
    if low == high:
        if array[low] == element:
            return low
        else:
            return -1
    
    if low < high:
        mid  = (low + high) // 2
        if element == array[mid]:
            return mid
        elif element < array[mid]:
            if element >= array[low]:
                return Search(array, element, low, mid - 1)
            else:
                return Search(array, element, mid + 1, high)
        else:
            if element <= array[high]:
                return Search(array, element, mid + 1, high)
            else:
                return Search(array, element, low, mid - 1)
            
    return -1

array = list(map(int, input("Enter list").split()))
element = int(input("Enter element"))
print(Search(array, element, 0, len(array) - 1))