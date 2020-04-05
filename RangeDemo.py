# Reference : Durga Software Solutions.
'''
In Python range() function and range data types both are available
It represents sequence of numbers.
range data type is an immutable
argument for range data type is int only.
If float is given then below exception occurs.
TypeError: 'float' object cannot be interpreted as an integer
'''

# range demo
# Form-1 : range(n)
# where n is int and represents the value from 0 to n-1

r = range(10)
print(type(r))
# <class 'range'>
for i in r:print(i)
# 0
# 1 ... 9
# Access the value by index.
print(r[2])
# 2
print(r[-2])
# 8
print(r[2:5])
# range(2, 5)
# r[0] =70 # uncomment this line to execute, if executed then below error will be thrown.
# TypeError: 'range' object does not support item assignment

# Form-2 : range(n1,n2)
# where n1,n2 = int and n2 = n2-1
r1 = range(30,50)
for i in r1:print(i)

# Form-2 : range(n1,n2,increment step)
# where n1,n2 = int and n2 = n2-1
for i in range(10,50,5) : print(i)
# 10 15 20 25 30 35 40 45


