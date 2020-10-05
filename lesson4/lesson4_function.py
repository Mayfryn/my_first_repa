def add(x, y):
    """this is documentation string - create the description of function add"""
    return x + y


print(add(2, 89))
print(add('jdf', 'jack'))
help(add)


def repeat(s, exclaim):
    res = s * 3
    if exclaim:
        return res + '!!!'
    return r


r = repeat('wow', True)
print(r)


def word_printer(word, count=1, wow=0):
    if wow == 1:
        return (word * count).upper()
    else:
        return word * count


z = word_printer('run', count=4, wow=1)
print(z)


def func(*args): #*args - takes how many you want arguments
    return args


print(func(1, 2, 3, 4, 5, 6, 'ewfwqre')) #tuple


def function(*args):
    k = list(args)
    index = 0
    k.sort()
    return k[1]
print(function(23, 434, 7, 0, 0, 0,  8347))

def func1(**kwargs):
    return kwargs
print(func1(r=5,f=6))

def dicto(**kwargs):
    return '{} is {}'.format(kwargs.get(),kwargs.get())
print(dicto(r=5,f=6))