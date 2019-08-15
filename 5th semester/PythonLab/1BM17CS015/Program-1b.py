#Fibonacci nummbers

def fibonacci(number):
    series = [0 for _ in range(number + 2)]
    series[1] = 1
    for i in range(2, number + 1):
        series[i] = series[i - 1] + series[i - 2]
    return series[number]

number = int(input("Enter the number: "))
fibonacciNumber = fibonacci(number)
print("The fibonacci number is", fibonacciNumber)
