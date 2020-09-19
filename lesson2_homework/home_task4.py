def task_header(task_number):
    print(" #{0} ".format(task_number).center(100, '='))

d = {
    "title": "applepie",
    "price": 12,
    "ingredients": ['apple', 'cinamon', 'flour', 'egg']
}
print(d)

#Task1
task_header(1)
d["desciption"] = "sooo yammy!!!"
print(d)

#Task2
task_header(2)
l = d.get("price")
l += 100
d.update({"price": l})
print(d)

#Task3
task_header(3)
i = d.get("ingredients")
i.append('sugar')
d.update({"ingredients": i})
print(d)

#Task4
task_header(4)
i = d.get("ingredients")
print('ingridients =', len(i))

#Task5
task_header(5)
d.pop("desciption")
print(d)
