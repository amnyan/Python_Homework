def change(ls):
    size = len(ls)
    for i in range(size):
        ls[i] /= size
        
    return ls

ls = [1,2,3,4,5,6,7,8,9,10]
new_ls = change(ls)
print(new_ls)