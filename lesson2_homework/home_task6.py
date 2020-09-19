a = float(input("Enter a first side: ".center(25)))
b = float(input("Enter a second side: ".center(25)))
c = float(input("Enter a third side: ".center(25)))

if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")