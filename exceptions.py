def exception(S):

    try:
        S = int(S)
    except:
        S = "Bad String"
    return S

S = raw_input().strip()
print exception(S)
