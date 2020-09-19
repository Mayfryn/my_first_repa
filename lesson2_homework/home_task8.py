a = float(input("Enter a first number:  "))
b = float(input("Enter a second number: "))
c = float(input("Enter a third number:  "))

if a == b == c:
    print(3)
if a == b or b == c or a == c:
    print(2)
if a != b and b!= c and c != a:
    print(0)