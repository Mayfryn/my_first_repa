print('miu-miu')
print("""I want
to jump""")

letters = ['a', 'b','c']
for i in letters:
    print(i)

# i = 1
# while i <= 10:
    # if i == 3:
    #     print("Skip 3")
    #     continue
    # print(i)
   

l = []
i = 1
while i <= 10:
    print(i)
    i += 1
    if i == 3:
        i += 1
        continue

    l.append(i)

print(l)
