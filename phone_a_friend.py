def phone_lookup():

    n = int(raw_input())
    i = 1
    phone_numbers = {}

    while i <= n:

        numbers = raw_input().strip().split(" ")
        phone_numbers[numbers[0]] = numbers[1]
        i += 1

    while True:

        numbers = raw_input().strip()

        if not numbers:
            break

        if not phone_numbers.get(numbers, 0):
            print "Not found"

        else:
            num = phone_numbers.get(numbers, 0)
            print "{}={}".format(numbers, num)

phone_lookup()
