number = int(input("Enter a number"))
divisors = [x for x in range(1, number + 1) if number % x == 0]
for x in divisors:
    print(x, end=" ")
