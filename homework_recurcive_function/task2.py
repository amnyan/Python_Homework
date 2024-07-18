# Write a recursive function to print numbers from 5 to 1.
def print_one_to_number(number):
    if number == 0:
        return
    
    print(number)
    print_one_to_number(number - 1)
    
    

print_one_to_number(5)