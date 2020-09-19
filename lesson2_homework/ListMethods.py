ls = [1, 2, 3, 4, 5, 6, 7]
l = [1, 2, 3, 4, 5, 6, 7]
mk = [0.0, 3.434, 'jfgh',[1, 2, 3], [4, 5, 6], 'OIKN']


# list.append(x)
# Add an item to the end of the list. Equivalent to a[len(a):] = [x].
ls.append(8)
print(ls)


# list.extend(iterable)
# Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.
ls.extend(mk)
print(ls)


# list.insert(i, x)
# Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
mk.insert(4, [34, 574])
print(mk)


# list.remove(x)
# Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
ls.remove('OIKN')
print(ls)

# list.pop([i])
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)
ls.pop(-1)
print(ls)


# list.clear()
# Remove all items from the list. Equivalent to del a[:].
la = ls
print(la)
la.clear()
print(la)

# list.index(x[, start[, end]])
# Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.
print(mk.index('jfgh'))


# list.count(x)
# Return the number of times x appears in the list.

print(l.count(3))
# list.sort(key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

# list.reverse()
# Reverse the elements of the list in place.
l.reverse()
print(l)


# list.copy()
# Return a shallow copy of the list. Equivalent to a[:].
n = l.copy()
print(n)