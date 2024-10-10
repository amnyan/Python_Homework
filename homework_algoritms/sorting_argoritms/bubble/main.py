#Bubble Sort O(n ^ 2)   O(1)

data = [1,2,3,6,4,8,5,7,9,10]


def bubble_sort(data:list)->list:
    flag = True
    while(flag):
        flag = False
        
        for i in range(len(data) -1):
            if (data[i + 1] < data[i]):
                data[i], data[i + 1] = data[i + 1],data[i]
                flag = True
    return data

print(data)
print(bubble_sort(data))
    
    