def task_header(task_number):
    print(" #{0} ".format(task_number).center(100, '='))
task_header(1)
def correct_input(n):
    if n.isnumeric():
        pass
    else:
        print("Enter the correct number")
    return n
correct_input(n=5)