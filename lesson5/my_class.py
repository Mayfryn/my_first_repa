class MyClass(object):
    def __init__(self):
        self.search = 'result'

    def my_method(self, add=''):
        print(self.search + add)


obj = MyClass()
obj.my_method()
obj.my_method(add='!')
print(obj.search)

m = 'tight'
help(m)
