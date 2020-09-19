x = 10
while x > 0:
    print(str(x) + '!')
    x -= 1

l = [1, 10, 3, 5, 6, 7, 11]
even = []
odd = []

for item in l:
    if item % 2 == 0:
        even.append(item)
    elif item %2 == 1:
        odd.append(item)
print(odd, even)

l = [1, 2, 3, 4, 5]

while l != []: #while l, while len(l) != 0
    print(l)
    l = l[0:-1] #print(l.pop())

a = int(input("Enter a number: "))
i = 0
while a % 2 == 0:
    print(int(a))
    a /= 2
    i += 1
print(i)

l = [78, 97, 31, 12, 99]

for i in l:
    if i % 2 == 0:
        print(i)
    if i % 2 == 1:
        l[l.index(i)] = i+1
        print(i+1)
print(l)

x = list(range(2,10))
print(x)

for i in range(1,1230,150):
    print(i, end = ', ')

for i in range(len(x)):
    if x[i] % 2 == 1:
        x[i] += 1
print(x)
