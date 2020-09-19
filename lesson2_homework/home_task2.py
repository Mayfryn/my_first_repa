def task_header(task_number):
    print(" #{0} ".format(task_number).center(100, '='))


#Task1
task_header(1)
a = (367**2+127**2)**0.5
print("hypotenuse =",a)

#Task2
task_header(2)
n = input("Enter number(<100):")
if 0 <= int(n) <= 10:
    print("The number has", int(n) // 10, "tens")
else:
    print("Enter the correct number")

#Task3
task_header(3)
n = input("Enter number(from 100 to 999):")
if 99 < int(n) < 1000:
    print("The sum of number digits is", int(n[0])+int(n[1])+int(n[2]))
else:
    print("Enter the correct number")

#Task4
task_header(4)
n = input("Enter integer nuber:")
if int(n) % 2 == 0:
    print(int(n))
else:
    print(int(n) + 1)

#Task5
task_header(5)
n = input("Enter real positive number:")
print(float(n) % 1)

#Task6
task_header(6)
n = input("Enter real positive number:")
print(int(float(n) % 1 *10 - float(n) % 1 *10 % 1))