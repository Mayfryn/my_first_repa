# try:
#     s = input("Enter some string: \n")
#     a = len(s)
#     if a % 2 == 0:
#         m = int(a/2)
#         s1 = s[:m]
#         s2 = s[m:]
#     else:
#         l = int((a+1)/2)
#         s1 = s[:l]
#         s2 = s[l:]
#     print(s1, s2)
#     r = s2 + s1
#     print(r)
# except IndexError:
#     print("You've entered too short string")


try:
    s = input("Enter string: \n")
    a = round(len(s)/2)
    s1 = s[:a]
    s2 = s[a:]
    print(s2+s1)
except IndexError:
    print("You've entered too short string")
