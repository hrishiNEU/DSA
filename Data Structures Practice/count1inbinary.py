def convert_to_bin(n):
    elements = []
    for i in range(n):
        bin_value = bin(i)[2:]
        str_bin_value = str(bin_value)

        no_of_1 = count_ones(str_bin_value)
        elements.append(no_of_1)

    print(elements)

def count_ones(bin_value):
    count = 0
    for i in bin_value:
        if i == "1":
            count+=1
    return count


convert_to_bin(4)