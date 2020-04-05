# Reference : Durga Software Solutions.
'''
Theory:
List and Tuple
If user to want to store group of values as single entity where
-> Insertion order is preserved.
-> Duplicates are allowed.
-> Heterogenous elements are allowed.
-> None (NULL in Java) is also allowed.
-> list can automatically increased or decreased automatically.
-> list Values / Elements are enclosed in [].
-> tuple Values / Elements are enclosed in ().
-> list and tuple are same except list is mutable but tuple is immutable.
'''

# list Demo
l=[]
print(type(l))
# <class 'list'>
# Add the value in list.
l.append(11)
l.append(12)
l.append(13)
l.append(11)
l.append(None)
l.append('Python')
print(l)
# [11, 12, 13, 11, None, 'Python']

# Access the elements of list.
print(l[0])
# 11
print(l[-2])
# None
print(l[1:4])
# [12, 13, 11]
l[2]= 33
print(l)
# [11, 12, 33, 11, None, 'Python']
# Remove the element from list.
l.remove(l[0])
print(l)
# [12, 33, 11, None, 'Python'] Here we can observer that element 11 is removed.

# Repetition Operator.
list = [100,'Python',True]
list1 = list*3
print(list1)
# [100, 'Python', True, 100, 'Python', True, 100, 'Python', True]

# tuple Demo
t = ()
print(type(t))
# <class 'tuple'>
t = (21,22,'Python',True,None,34.6)
print(t)
# (21, 22, 'Python', True, None, 34.6)
# t[0] = 31 # Uncomment this line to execute, if executed it throws below error.
# TypeError: 'tuple' object does not support item assignment
t1 = t*2
print(t1)
# (21, 22, 'Python', True, None, 34.6, 21, 22, 'Python', True, None, 34.6)

t2 = (31,32,[33,34])
print(t2)
# (31, 32, [33, 34])