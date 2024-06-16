def sum_of_max_min(ls):
    max = ls[0]
    min = ls[0]
    for i in range(1,len(ls)):
        if ls[i] > max:
            max = ls[i]
        if ls[i] < min:
            min = ls[i]
    return max + min

ls = [1,5,2,3,0.1,10,0.9]
sum = sum_of_max_min(ls)
print(f"sum  is {sum}")