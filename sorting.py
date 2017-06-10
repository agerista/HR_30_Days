n = int(raw_input())
a = list(map(int, raw_input().strip().split(' ')))


# Write Your Code Here
def bubbleSort(n, a):

    numberOfSwaps = 0

    for i in range(n):
        # Track number of elements swapped during a single array traversal
        for j in range(n-1):
            # Swap adjacent elements if they are in decreasing order
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
                numberOfSwaps += 1

    # If no elements were swapped during a traversal, array is sorted
        if numberOfSwaps == 0:
            break

    statement = "Array is sorted in {} swaps. \nFirst Element: {} \nLast Element: {}".format(numberOfSwaps,                                                                                                  a[0], a[-1])
    return statement

print bubbleSort(n, a)
