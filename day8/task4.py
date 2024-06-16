def check(number,ls):
    return True if number in ls else False

ls = [0,1,2,3,4,5]
number = input("Please enter the number ")
if number.isnumeric():
    if (check(int(number), ls)):
        print("YES")
    else:
        print("NO")
else:
    print("Invalid Input")