def bitwise_and(n, k):

    if k | k-1 <= n:
        return k-1

    else:
        return k - 2

t = int(raw_input().strip())
for a0 in xrange(t):
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    print(bitwise_and(n, k))
