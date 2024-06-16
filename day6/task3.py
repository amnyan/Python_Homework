def max_item_index(ls):
    max_index = 0
    max = ls[0]
    for i in range(1,len(ls)):
        if ls[i] > max:
            max = ls[i]
            max_index = i
    return max_index

ls = [1,5,2,3,0,10,0.9]
index = max_item_index(ls)
print(f"maximum index is {index}")