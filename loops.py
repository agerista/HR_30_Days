def multiples(n):

    for i in range(1, 11):

        m = n * i
        print "{} x {} = {}" .format(n, i, m)


n = int(raw_input().strip())
multiples(n)
