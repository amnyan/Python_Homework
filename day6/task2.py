def min_item(ls):
    min = ls[0]
    for i in range(1,len(ls)):
        if ls[i] < min:
            min = ls[i]
    return min

ls = [1, 4.5, 8, 0.8, 3.8, 1.1]
minimum = min_item(ls) 
print(f"min : {minimum}")