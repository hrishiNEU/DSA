# def fibonacci(n):
#     total=1
#     for i in range(2,n):
#         total += i

#     print(total)

# fibonacci(6)

def fibonacci(n):
    a, b = 1, 0

    for i in range(n):
        temp =  a
        a = a + b
        b = temp
    
    print(a)

fibonacci(6)