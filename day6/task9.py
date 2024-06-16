def append(size):
    ls = []
    for i in range(size):
        number = input("Enter elements ")
        if (number.isdigit()):
            ls.append(int(number))
    return ls

count = input("Please enter size of elements ")
if count.isdigit():
    new_ls = append(int(count))
    print(new_ls)
else:
    print("Invalit Size ")
    
