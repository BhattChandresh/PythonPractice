# Reference : Durga Software Solutions.

# Default seperator is space.
# In Print statement if we want ',' as separator then below example.
print(10,20,30,sep=',')
print(10,20,30,40,sep=':') # : as separator

# end attribute.
# end attribute join two print statements with the separator provided by user.
print(1,2,3,4,end='****')
print(5,6,7,8)


# sep and end together
print(10,20,30,40,sep='^',end='>>>>')
print(50,60,70,80,sep='--')

# print (formatted string)
# Syntax : print("formatted string" %(arguments)
a,b,c = 5,7.8,45
print("a=%i" %a)
print("a=%i and b=%f" %(a,b))


name = 'Python'
l = [15,10,15,20,25]
print("Hello %s the list is %s" %(name,l))

# print with replacement operator
# {} = replacement operator
name = 'Python'
version = 3.0
hours = 120
print({"I am learing {0} version {1} in {2} hours".format(name,version,hours)})
print({"I am learing {} version {} in {} hours".format(name,version,hours)})
print({"I am learing {x} version {y} in {z} hours".format(z=hours,y=version,x=name)})



