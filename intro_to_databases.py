# Non-regex version
def is_gmail(n_list):

    gmail = []

    for i in n_list:
        if i[1][-10:] == "@gmail.com":
            gmail.append(i[0])
    gmail.sort()
    return ' \n'.join(gmail)

N = int(raw_input().strip())
n_list = []

for a0 in xrange(N):

    firstName, emailID = raw_input().strip().split(' ')
    firstName, emailID = [str(firstName), str(emailID)]
    n_list.append([firstName, emailID])

print is_gmail(n_list)

# regex version coming soon!
