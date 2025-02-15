arr = [23,454,231,3,545,2,11,33,765]

def bubblesort(arr, n):
    if n == 1:
        return arr
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        
    return bubblesort(arr, n-1)

print(bubblesort(arr, len(arr)))
