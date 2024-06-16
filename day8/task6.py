def rearrange_even_odd(arr):

    start = 0
    end = len(arr) - 1

    result = [0] * len(arr)
    
    for num in arr:
        if num % 2 == 0:
            result[start] = num
            start += 1
        else:
            result[end] = num
            end -= 1
    
    return result

array = [1, 2, 3, 4, 5, 6, 7, 8,9,10]
new_array = rearrange_even_odd(array)
print("old array:", array)
print("new array:", new_array)
