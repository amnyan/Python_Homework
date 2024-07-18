# Write a recursive function to print all elements of a list.

def print_list(ls):
    if not ls:
        return
    
    print(ls[0])
    print_list(ls[1:])
    
    
# ls = [1,2,3,4,5,6,7,8,9,10]
ls = []
print_list(ls)