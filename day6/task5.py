def sum_of_max_min(ls):
    max_index = 0
    max = ls[0]
    min_index = 0
    min = ls[0]
    for i in range(1,len(ls)):
        if ls[i] > max:
            max = ls[i]
            max_index = i
        if ls[i] < min:
            min = ls[i]
            min_index = i
    return max_index, min_index

ls = [1,5,2,3,0,10,0.9]
max,min = sum_of_max_min(ls)
print(f"maximum index is {max}\nminimum index is {min}")