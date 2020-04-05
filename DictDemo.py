# Reference : Durga Software Solutions.

'''
Theory:
-> If you want to represent the elemets as key/value pairs use dict data type.
-> Like word -> meaning, empid->empname.
-> Keys must not be duplicated but values may be duplicated.
-> Dictionary elements are enclosed in {}.
-> Heterogenours keys and values are allowed.
-> Dictionary are mutable.
-> Insertion order is not preserved.
'''

# CREATE EMPTY DICTIONARY
dictionary = {}
print(type(dictionary))
# CREATE EMPTY SET
s = set()
print(type(s))

# Dict Demo
d = {1:'A',2:'B',3:'C',4:'A'}
print(type(d))
# <class 'dict'>
print(d)
# {1: 'A', 2: 'B', 3: 'C', 4: 'A'}


# Add the elements in Dictionary.
d[5] = 'R'
print(d)
# {1: 'A', 2: 'B', 3: 'C', 4: 'A', 5: 'R'}

# NOTE: IF KEY ARE DUPLICATED IN DICTIONARY THEN THERE WON'T BE ANY ERROR
# IN THIS SITUATION, OLD VALUE WILL BE REPLACED WITH NEW VALUE.

d[1] = 'ABC'
print(d)
# {1: 'ABC', 2: 'B', 3: 'C', 4: 'A', 5: 'R'}