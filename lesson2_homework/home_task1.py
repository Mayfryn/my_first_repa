s = "the tes ter s"
s1 = "      23585      "
m = "8742834"
h = "H.o.m.e.w.o.r.k"
i = "Interesting"
k = "Hi! My name is Mayfryn"
def task_header(task_number):
    print(" #{0} ".format(task_number).center(100, '='))

#Task1
task_header(1)
print (s.isnumeric())
print (m.isnumeric())

#Task2
task_header(2)
print(s.count(' '))

#Task3
task_header(3)
print(h.count('.'))

#Task4
task_header(4)
c = "Homework"
print(c.center(100))
print(len(c.center(100)))

#Task5
task_header(5)
print(s.capitalize())

#Task6
task_header(6)
print(i.endswith('ing'))
print(h.endswith('ing'))

#Task7
task_header(7)
print(k.find('a'))

#Task8
task_header(8)
print(s.rsplit(' '))

#Task9
task_header(9)
print(s1.strip(' '))