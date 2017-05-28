def reverse_array(arr):

    arr[::] = arr[-1::-1]
    arr = map(str, arr)
    print " ".join(arr)

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
reverse_array(arr)
