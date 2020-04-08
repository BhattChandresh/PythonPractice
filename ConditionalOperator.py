# Reference : Durga Software Solutions.

# Conditional Operator in Python
x= 30 if(10 <20) else 40
print(x) # 30
x=True if(100 > 90) else False
print(x) # True
x=True if(10 > 90) else False
print(x) # False

# To take the Input from Keyboard we need to user the function input().
# When we ask the input from user, enter values always be in String
# We need to perform type casting to convert it to compatible type.
a = int(input("Enter First Number(a):"))
b = int(input("Enter Second Number(b):"))
minValue = a if a < b else b
print("Minimum Value:", minValue)

# Nesting of conditional Operator.
x = 10 if 20 < 30 else 40 if 50 < 60 else 70
print(x) # 10

x = 10 if 20 > 30 else 40 if 50 > 60 else 70
print(x) # 70

a = int(input("Enter First Number(a):"))
b = int(input("Enter Second Number(b):"))
c = int(input("Enter Third Number(c):"))
maxValue = a if a > b and a > c else b if b > c else c
print("Maximum Value:", maxValue)