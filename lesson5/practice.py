class Person:  # класи називають з великої літери(CamelCase)
    # common_attr = []

    def say_hello(self):  # функції називаються з маленької літери з нижнім підкресленям(Snake Case)
        print("Hello!")

    def print_self(self):
        print(self)

    def set_name(self, n, s):
        self.name = n
        self.surname = s


p1 = Person()
p2 = Person()

# p1.say_hello()
# p2.say_hello()
# print(p1.common_attr)
# p1.common_attr.append("Earth") # мміняємо для всіх
# print(p2.common_attr)
# p1.print_self()
# p2.print_self()
# print(p1)
# print(p2)

p1.set_name("Alison", "Adams")
p2.set_name("Beatrix", "Bull")
print(p1.name, p1.surname)
print(p2.name, p2.surname)

# class Animal:  # класи називають з великої літери(CamelCase)
#     # common_attr = []
#
#     def say_hello(self):  # функції називаються з маленької літери з нижнім підкресленям(Snake Case)
#         print("Hello!")
#
#     def print_self(self):
#         print(self)
#
#
# a1 = Animal()
# a2 = Animal()
#
# # p1.say_hello()
# # p2.say_hello()
# # print(p1.common_attr)
# # p1.common_attr.append("Earth") # мміняємо для всіх
# # print(p2.common_attr)
# a1.print_self()
# a2.print_self()
# print(a1)
# print(a2)
#
# class Test:
#     pass
# t = Test()
# print(t)
