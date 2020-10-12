class Person:
    """

    """
    common_attr = []
    def __init__(self, n, s, x, v=None):
        self.name = n
        self.surname = s
        self.age = x
        self.value = v

    def full_name(self):
        return "{} {}".format(self.name, self.surname)
        return f"{self.name} {self.surname}"
        return self.name + " " + self.surname


    def get_older(self, years):
        self.age += years

    def __str__(self):
        return f"<Person object with name={self.name}, age={self.age} and full={self.full_name()}"




p1 = Person("Ola","Lao", 10, 100)
print(p1.full_name())
p1.get_older(20)
print(p1.age)
print(p1)


class Employee(Person):
    """

    """

    def __init__(self, name='', surname='', age=None, position='', salary=0, ):
        pass