#Filter even numbers in a list
unfilteredList = list(map(int, input("Enter numbers:").split()))
evens = list(filter(lambda x : x % 2 == 0, unfilteredList))
print("The even numbers are: ")
for number in evens:
    print(number, end = " ")