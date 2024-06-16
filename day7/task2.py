def prime_number(number):
    if number < 1:
        print("Invalid Range")
        return -1
    if number == 1 or number == 2:
        return True
    i = 2
    while(i <= (number / 2)):
        if (number % i == 0):
            return False
        i += 1
    return True
TOP =100        
for i in range(TOP):
    if (prime_number(i)):
        print(i)