def task_header(task_number):
    print(" #{0} ".format(task_number).center(100, '='))


l = [10, 20, 30, 40, 50, 60, 70, 80, 90]
l4 = [114, 39, 35, 0, 5753, 435]
s = "123456789"
seq = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 0]

# Task1
task_header(1)
while l:
    print(l)
    l = l[1:]

# Task2
task_header(2)
while s:
    print(s)
    s = s[1:]

# Task3
task_header(3)
print(l4)
l4.sort()
while l4:
    print(l4[0])
    l4 = l4[1:]

# Task4
task_header(4)
i = 0
count = 1
max_count = 0

while seq[i] != 0:
    while seq[i] == seq[i + 1]:
        count += 1
        i += 1
    max_count = max(max_count, count)
    count = 1
    i += 1

print(seq)
print(max_count)