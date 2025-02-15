def dec_to_bin(n):
    binary = bin(n)
    bin_value = binary[2:]

    length = len(bin_value)

    str_bin_value = str(bin_value)

    ttb = ""

    leading_zeros = 32 - length

    for i in range(leading_zeros):
        ttb += "0"

    for i in range(length):
        ttb += str_bin_value[i]

    rev_ttb = ttb[::-1]

    print(rev_ttb)

    answer = int(rev_ttb, 2)

    print(answer)

dec_to_bin(2)