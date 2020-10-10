import t


myfile = open("first_file.txt", "r")
cont = myfile.read()
print(cont)
myfile.close()

file = open("first_file.txt")
file.write("")