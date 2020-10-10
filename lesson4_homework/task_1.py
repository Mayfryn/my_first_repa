def sing_my_song(str_count=3, word_count=3, var=0):
    """Со значениями по умолчанию
Пишем функцию, которая генерирует песню la-la-la. Функция принимает 3 аргумента:

1-е число – сколько строк будет в песне. По умолчанию 3
2-е число – сколько «la» будет в строке («la» в строке объединяются дефисом). По умолчанию 3
3-е число – если 0, то в конце песни (в конце последней строчки) стоит точка, если 1, то в конце стоит «!». По умолчанию 0
"""
    assert var in [0, 1], "Please choose 0 or 1 for var paremeter"
    ending_symbols = ['.', '!']

    sitr = "la"
    i = 1
    while i < word_count:
        i += 1
        sitr += "-la"


    while str_count-1:
        print(sitr)
        str_count -= 1
    print(sitr, end=ending_symbols[var])


sing_my_song(10, 10, 1)
