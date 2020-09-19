while True:
    print("Type 'quit' to exit")
    phrase = input("Your message: ")
    if phrase == "quit":
        break
    elif phrase == "Hello" or phrase == "Hi":
        print("Hi! How are you?")
    elif phrase == "What is your name?":
        print("I'm robot")
    else:
        print("I don't understand you...")

print("Enter the WORD, pls")
while True:
    word = input("the WORD is: ")
    if word.count(' ') == 0:
        break
    else:
        print("Enter the WORD without spaces")

print(word)

print("Enter the WORD, pls")
while True:
    word = input("the WORD is: ")
    m = word.lstrip().rstrip()
    if m.count(' ') == 0:
        break
    else:
        print("Enter the WORD without spaces")

print(word)


s = input("Enter: ")

try:
    s = int(s)
    print(s)
except:
    print("Error")

s, i = 's', 0
try:
    int(s)/i
except ValueError as e:
    print(e)
except ZeroDivisionError:
    print("Do not divide")


while True:
    s = input("Enter: ")
    try:
        s = float(s)
        print(s)
        break
    except ValueError:
        print("Enter a number: ")