def min_item_index(ls):
    min_index = 0
    min = ls[0]
    for i in range(1,len(ls)):
        if ls[i] < min:
            min = ls[i]
            min_index = i
    return min_index

ls = [1,5,2,3,0,10,0.9]
index = min_item_index(ls)
print(f"minimum index is {index}")