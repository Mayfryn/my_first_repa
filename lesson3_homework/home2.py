try:
    s = input("Enter some string: \n")
    a = len(s)
    if a % 2 == 0:
        m = int(a/2)
        s1 = s[:m]
        s2 = s[m:]
    else:
        l = int((a+1)/2)
        s1 = s[:l]
        s2 = s[l:]
    print(s1, s2)
    r = s2 + s1
    print(r)
except IndexError:
    print("You've entered too short string")