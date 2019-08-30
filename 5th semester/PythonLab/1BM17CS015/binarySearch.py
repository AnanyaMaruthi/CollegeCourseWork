def binarySearch(arr, low, high, element):
	print(low, high)
	if(low <= high):
		mid = (low + high) // 2
		print(mid)
		if(arr[mid] == element):
			return (True)
		elif(arr[mid] < element):
			low = mid + 1
			return binarySearch(arr, low, high, element)
		else:
			high = mid - 1
			return binarySearch(arr, low, high, element)		
	return False
	
array = list(map(int, input("Enter elements").split()))
element = int(input("Enter element"))
print(binarySearch(array, 0, len(array) - 1, element))

