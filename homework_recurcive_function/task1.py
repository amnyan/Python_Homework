# Write a recursive function to print numbers from 1 to 5.

def print_one_to_number(number):
    if number == 0:
        return
    
    print_one_to_number(number - 1)
    print(number)
    

print_one_to_number(5)