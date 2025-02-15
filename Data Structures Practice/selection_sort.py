def selection(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

array1 = [3,7,5,3,8,0,4,2]

print("Unsorted array", array1)

sorted_array = selection(array1)

print("Sorted array: ",sorted_array)

def selection_sort_recursive(arr, index=0):
    if index == len(arr):
        return arr
    
    min_index = index

    for j in range(index+1,len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[index], arr[min_index] = arr[min_index], arr[index]
    return selection_sort_recursive(arr,index+1)

array2 = [4,8,3,2,1,8,7,5,6]

print("Unsorted array for recursion",array2)

sorted_array_recursive = selection_sort_recursive(array2)

print("Sorted array using recursion",sorted_array_recursive)