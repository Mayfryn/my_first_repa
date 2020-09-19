a = float(input("Enter a first number:  "))
b = float(input("Enter a second number: "))
c = float(input("Enter a third number:  "))

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print(a,'<', b,'<', c)