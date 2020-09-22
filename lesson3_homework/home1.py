# try:
#     s = input("Enter some string: \n")
#     print(s[2], s[-2], s[:5], s[:-2],s[::2], s[1:-1:2], s[::-1], s[::-2], s[-2::-2],s[-2:0:-1], sep='\n')
# except IndexError:
#     print("You've entered too short string")

try:
    s = input("Enter some string: \n")
    tasks = [s[2], s[-2], s[:5], s[:-2],s[::2], s[1:-1:2], s[::-1], s[::-2], s[-2::-2],s[-2:0:-1]]
    for i in range(len(tasks)):
        print("#{}.  {}".format(i + 1, tasks[i]))
except IndexError:
    print("You've entered too short string")