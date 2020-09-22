a = input("Enter a first value:  ")
b = input("Enter a second value: ")
try:
    print(int(a) + int(b))
except ValueError:
    print(a + b)