while True:
    word = input("the WORD is: ")
    m = word.strip()
    if m.count(' ') == 0:
        break
    else:
        print("Enter the WORD without spaces")

print(word)