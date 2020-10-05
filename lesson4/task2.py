def hypotenuse(x, y):
    res = (x ** 2 + y ** 2) ** 0.5
    return res


print(hypotenuse(3, 4))
print(hypotenuse(4, 4))
print(hypotenuse(1, 2))


def dell_numbers(s):
    for i in s:
        if not i.isalpha():
            res = s.replace(i, "")
            s = res
    assert res.isalpha(), "something went wrong! Check your function! "
    return res


print(dell_numbers('12dggf656 uygu'))
