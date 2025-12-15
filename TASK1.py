#TASK1
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result = result * i
    return result

number = int(input("Type any number of your choice : "))
factorial = factorial(number)

print(f"Factorial of {number} is: {factorial}")
