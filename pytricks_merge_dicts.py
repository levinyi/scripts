#How to merge two dicts in python 3.5+
x = {'a' : 1, 'b' : 2}
y = {'b' : 3, 'c' : 4}

z = {**x, **y}
print(z)

# if dict has key, value add/mul/sub ....

# if dict has key, value stored as a list.

# if dict has key value stored as a tuple.

# and so on.
