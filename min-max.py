def min(arr):
    min_num=arr[0]
    for i in arr:
        if i<min_num:
            min_num = i
    return min_num
    
def max(arr):
    max_num = arr[0]
    for i in arr:
        if i>max_num:
            max_num = i
    return max_num