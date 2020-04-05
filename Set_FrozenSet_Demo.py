# Reference : Durga Software Solutions.

'''
Theory:
If you want to represent group of elements as single entity where
-> Insertion order are not preserved.
-> Duplicates are not allowed.
-> Values / elements are represented in {}.
-> Indexing / Slicing are not applicable set.
-> Heterogenous objects are allowed.
-> set is mutable.
-> set and frozenset are same except set is mutable while frozenset is immutable.
'''

# set demo

s = {21,22,23,25,21,22,23}
print(s) # Insertion order not preserved and duplicates are removed automatcially.
# {25, 21, 22, 23}
print(type(s))
# <class 'set'>
# print(s[0]) # uncomment this line to execute, if executed then below error will be thrown.
# TypeError: 'set' object does not support indexing
# print(s[1:3]) # uncomment this line to execute, if executed then below error will be thrown.
# TypeError: 'set' object is not subscriptable


# Add the element in Set.
s.add('Python')
s.add(True)
print(s)
# {True, 'Python', 21, 22, 23, 25}

# Remove the element from Set.
s.remove(25)
print(s)
# {True, 'Python', 21, 22, 23}

s = {10,20,30,40}
fs = frozenset(s)
print(type(fs))
# <class 'frozenset'>
print(fs)
# frozenset({40, 10, 20, 30})

# try to mutate(Add/Remove) the frozenset will throws the error.
# fs.add(50) # uncomment this line to execute, if executed then below error will be thrown.
# AttributeError: 'frozenset' object has no attribute 'add'