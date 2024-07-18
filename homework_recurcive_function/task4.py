# Write a recursive function to find the sum of the first N natural numbers.

def sum_of_N_number(number):
    if (number < 1):
        return 0
    return number + sum_of_N_number(number - 1)


number = input("Please enter the number : ")
if number.isdigit():
    print(f"Sum of the first {number} is {sum_of_N_number(int(number))}")
else:
    print("Invalid Number!!!")