a = 23
b = 434

print(int(a) + int(b))


print(a, b, 10.0, 'Spam', sep = ',')
print(a, b, 10.0, 'Spam', sep = '\n')
print(a, b, 10.0, 'Spam', sep = '', end = '\n')

print(a, b, end = ', ')
print('ehf', 'ewpfo')


s = "Hi there! How are you?"
print(s[2:7])
print(s[:10])
print(s[0:-3:2])
print(s[::-1])
print(s[2:8:-1])
print(s[8:2:-1])

l = [1, 3.14, "Hello", [5, 7, "people"]]
l[1] = 2.71
l[1:2] = [10, 11, 12]
print(l)
l[2:2] = ["eggs", "spam"] #insert on 2 place
print(l)

