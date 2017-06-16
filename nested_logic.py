def library_fines(returned, expected):
    """Note: there is only a fine for year or months or days, do not add months
    and days"""

    fine = 0

    y = int(returned[2]) - int(expected[2])
    m = int(returned[1]) - int(expected[1])
    d = int(returned[0]) - int(expected[0])

    if y > 0:
        return 10000

    if y == 0:
        if m > 0:
            return 500 * m

        elif m == 0:
            if d > 0:
                return 15 * d

    return fine

returned = raw_input().strip().split(" ")
expected = raw_input().strip().split(" ")
print library_fines(returned, expected)
