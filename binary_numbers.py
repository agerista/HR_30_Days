def binary(n):

    b2 = list(bin(n).replace("0b", ""))
    max = 0
    ones = 0

    for char in b2:

        if char == "1":
            ones += 1
            if max < ones:
                max = ones
        else:
            # reset ones when 0 encountered
            ones = 0
    return max

n = int(raw_input().strip())
print binary(n)
