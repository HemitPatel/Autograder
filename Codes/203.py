def rotate_array(arr, k):
    n = len(arr)
    
    for i in range(k):
        temp = arr[n-1]
        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = temp
        
    return arr

print(rotate_array([1,2,3,4,5], 2))
