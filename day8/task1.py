def max_string(ls):
    max = len(ls[0])
    max_index = 0
    for i in range(1,len(ls)):
        size = len(ls[i])
        if size > max:
            max = size
            max_index = i
            
    return max,max_index

ls = ['Hello', "Bye", "Yes","Okay","Abraham"]
max,index = max_string(ls)
print(f"max : {max}\nindex : {index}")