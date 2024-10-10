#Selection Sort O(n * (n - 1))   O(1)

data = [1,5,3,2,7,4,9,8,10,6]

def selection_sort(data:list)->list:
    data_len = len(data)
    for i in range(data_len):
        min_index = i
        for j in range(i + 1, data_len):
            if (data[j] < data[min_index]):
                min_index = j
    
        data[i], data[min_index] = data[min_index],data[i]
    
    return data


print(data)
print(selection_sort(data.copy()))