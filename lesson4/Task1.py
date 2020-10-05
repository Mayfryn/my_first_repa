s = ['dfs', 'ewsafd', 'ewfweffddzfdg', 'fknvgkjfd']
j = 0
for i in s:
    if len(i)%2 !=0:
        j += 1
print(j)

d = {1:2, 3:4, 5:6}
for key, value in d.items():
    print(key, ": ", value, sep='')
    print(type(key), type(value))