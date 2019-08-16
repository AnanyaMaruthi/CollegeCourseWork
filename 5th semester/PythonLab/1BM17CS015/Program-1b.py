#Fibonacci nummbers

def fibonacci(number):
    series = [0 for _ in range(number)]
    try:
        series[0] = 0
        series[1] = 1
    except:
        return series
    for i in range(2, number + 1):
        series[i] = series[i - 1] + series[i - 2]
    return series

number = int(input("Enter the number: "))
series = fibonacci(number)
print("The fibonacci series is")
for x in series:
    print(x, end = " ")
