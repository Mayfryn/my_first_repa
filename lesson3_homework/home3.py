def task_header(task_number):
    print(" #{0} ".format(task_number).center(100, '='))

#Task1
task_header(1)
i = 0
while i <= 10:
    print(i)
    i += 1

#Task2
task_header(2)
i = 20
while i > 0:
    print(i)
    i -= 1

#Task3
task_header(3)
a = int(input("Enter a number: \n"))
i = 0
while a % 2 == 0:
    print(int(a))
    a /= 2
    i += 1
print(i)