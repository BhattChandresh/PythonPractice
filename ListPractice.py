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

# CREATION OF LIST OBJECTS
# Create empty list object
l = []
print('Empty List:',l)
print(type(l))

l = [10,10.5,'Python',True]
print('List :',l)

l = eval(input('Enter List:'))
print('List entered through Keyboard:',l)

l = list(range(0,100,5))
print(l)

l = list('Chandresh')
print(l)


# Access the elements of List
# 1. By using index.
# 2. By using slice operator.

l = [10,20,[30,40]]  # Nested List
for x in range(0,len(l)):
    print(l[x])
print(l[-2]) #20

l = [10,20,30,40,50,60]
print(l[::2])
print(l[::-1])

# Traversing the list
# By using while loop:
list = [5,10,15,20,25,30,35,40,45,50]
i = 0
while i < len(list):
    print(list[i])
    i +=1
# By using for loop:
list = [2,4,6,8,10,12,14,16,18,20]
for x in list:
    if x % 2 == 0:
        print("{} is even no".format(x))
    else:
        print("{} is odd no".format(x))

list =['A','B','C','D','E']
i = 0
while i < len(list):
    print('Element at positive index:',i,'->',list[i])
    print('Element at negative index:',i-len(list),'->',list[i-len(list)])
    i = i+1

# Important functions and methods of List:
# 1. len(list) [function]
# 2. count()   [method]
# 3. index()   [method] return the first occurrence of element

list = [10,20,30,40,50,60,10,10,10,20]
print('Length of the list:',len(list))
print('No of occurrence of element 10:',list.count(10))
print('No of occurrence of element 20 :',list.count(20))
print('First index of element 10 :',l.index(10))
print('First index of element 60 :',l.index(60))
target = int(input('Enter the value to search in list:'))
if target in l:
    print(target," available in list and first position at ",l.index(target))
else:
    print(target,"not available in list")


# Manipulating elements of list:
# 1. append [method] used to add the element to list
l=[]
l.append('Sachin')
l.append('Virat')
l.append('Mahi')
l.append('Rohit')
l.append('Hardik')
print(l)

l=[]
for x in range(101):
    if x%10==0:
        l.append(x)
print(l)

# 2. insert(index,element) add the element at particular index.
l.insert(2,1000)
print(l)

# 3. list1.extends(list2) add all the elements of list2 to list1
l1=['Health','Physical Fitness','Mental Fitness']
l2 =['Food','Exercise','Meditation']
l1.extend(l2)
print("List1:",l1)
print("List2:",l2)