def even_odd():

    for i in range(int(raw_input())):
        s = raw_input()
        print "".join(s[::2]), "".join(s[1::2])

even_odd()
