arr = [1,2,3,4,5]
length = len(arr)

def search(element, start, end) -> int:
    if (start > end):
        return -1

    middle = (start+end) // 2

    if(arr[middle] == element):
        return middle

    elif(arr[middle]>element):
        return search(element, start, middle-1)

    elif(arr[middle]<element):
        return search(element, middle+1, end)

value = search(6,0,length-1)
print(value)
