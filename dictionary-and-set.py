# d = {'k': 123, [1, 2, 3, 4]: 123}     # here [1,2,3,4] is a key of type list
# print(d[[1, 2, 3, 4, 5]])    # error -- key can only be an immutable type

# d = {'k': 123, (1, 2, 3, 4): 123, (1, 2, 3, 4, 5): list(str(123))}
# print(d[(1, 2, 3, 4)])     # here key is a tuple and is immutable, so no error
# print(dir(d))

# d = {'k': 123, (1, 2, 3, 4): 123, (1, 2, 3, 4, 5): list(str(123))}
# print(d[(1, 2, 3, 4, 5)])

"""
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
"""
# print(d.keys())
# print(d.values())
# print(d.items())  # gives a list of tuples -- [('k', 123), ((1, 2, 3, 4), 123), ((1, 2, 3, 4, 5), ['1', '2', '3'])]
# A dict is a mutable datatype

# d['k'] = 1234
# print(d)

# Set -- does not accept duplicates and does not inherit/have an order
s = {'a', 'a', 'b', 'c'}
# print(s)
# {'b', 'a', 'c'}
# s[0] = 'abc' # TypeError: 'set' object does not support item assignment
# print(dir(s))

"""
'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'
"""

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
print("bananaa" in thisset)
print("banana" not in thisset)