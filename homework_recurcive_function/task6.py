# Write a recursive function to find the length of a list.

def len_ls(ls):
    if not ls:
        return 0
    
    return 1 + len_ls(ls[1:])


ls = [1,2]
print(len_ls(ls))