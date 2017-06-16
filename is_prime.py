def is_prime(n):

    sqrt = n*n
    if n == 0 or n == 1:
        return "Not prime"

    if n == 2 or n == 3:
        return "Prime"

    if n % 2 == 0:
        return "Not prime"

    else:
        for x in range(3, sqrt, 2):
            if n % x == 0:
                return "Not prime"

        return "Prime"
