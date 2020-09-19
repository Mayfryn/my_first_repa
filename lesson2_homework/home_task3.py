l = ['alfa', 'beta', 'gamma', 'delta', 'epsilon', 'eta', 'teta', 'kappa']

def task_header(task_number):
    print(" #{0} ".format(task_number).center(100, '='))

#Task1
task_header(1)
print(l[-3])

#Task2
task_header(2)
print(l[1][0])

#Task3
task_header(3)
print(l[-1][-1])

#Task4
task_header(4)
l.append('ksi')
print(l)

#Task5
task_header(5)
l.insert(4, 'pi')
print(l)

#Task6
task_header(6)
l.remove(l[0])
print(l)

#Task7
task_header(7)
if 'word' in l:
    l.remove('word')
    print(l)
else: print("No such a wodr in this list")

#Task7_1
task_header(7_1)
if 'eta' in l:
    l.remove('eta')
    print(l)
else: print("No such a wodr in this list")