# Write a recursive function to calculate the factorial of a given number.

def factorial(number):
    if number < 0:
        return -1
    if number in [0,1]:
        return 1
    return number * factorial(number - 1)

number = input("Please enter the number : ")
if number.isdigit():
    print(f" Factorial of {number} is {factorial(int(number))}")
else:
    print("Invalid Number")