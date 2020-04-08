# Reference : Durga Software Solutions.

'''
Theory:
1. Arithmetic operator
    - Addition(+),
    - Substraction(-),
    - Multiplication(*),
    - Division(/),
    - Modulo(%),
    - Floor Division operator(//),
    - Power / Exponent operator(**)
    + operator can also be used for string concatenation but make sure that both the arguments are of string type.
    * operator can also be used for string repetition
      'String'*(N) where N should be integer only.

2. Relational operators or Comparison operators
   >,>=,<,<=
   This operators also applied to String and boolean types as well.
   For String Python compares the ASCII values of String.
   == (Equal method in Java) and != do the content comparison.
   Even the  chaining of operators are also applicable to == and !=.

3. Logical Operators.
   and, or , not

4. Bitwise Operators.
   &,|,^,~,>>,<<
   Above operators only applicable to only int and boolean types.

5. Assignment Operators.

6. Special Operators.


'''

print("--- Arithmetic Operators Demo ---")
a = 10
b = 2
print("a+b = ", a + b)  # a+b =  12
print("a-b = ", a - b)  # a-b =  8
print("a*b = ", a * b)  # a-b =  20
# Divison operator always return the float value.
print("a/b = ", a / b)  # a/b =  5.0
print("a%b = ", a % b)  # a%b =  0
# If both operands of int type then return value is int and
# if both operands of float type then return value is float Floor division.
print("a//b", a // b)  # a//b 5
print("a**b", a ** b)  # a**b 100

a = 10.5
b = 2
print("a+b = ", a + b)  # a+b =  12.5
print("a-b = ", a - b)  # a-b =  8.5
print("a*b = ", a * b)  # a-b =  21.0
print("a/b = ", a / b)  # a/b =  5.25
print("a%b = ", a % b)  # a%b =  0.5
# If one operands of int type and another one is of float type then return value is float.
print("a//b", a // b)  # a//b 5.0
print("a**b", a ** b)  # a**b 110.25

# s = 'Python' + 3 # uncomment this line to execute, if executed then below error will be thrown.
# TypeError: Can't convert 'int' object to str implicitly
s = 'Python' + '3'
print(s)  # Python3
print('Python' + str(3))  # Python3

print('Python3' * 2)  # Python3Python3
print(4 * 'Python2')  # Python2Python2Python2Python2
# print('Pyhton'* 1.0) # uncomment this line to execute, if executed then below error will be thrown.
# TypeError: can't multiply sequence by non-int of type 'float'

print("--- Relational Operators Demo ---")
a = 10
b = 20
print("a > b", a > b)  # a > b False
print("a >= b", a >= b)  # a >= b False
print("a < b", a < b)  # a < b True
print("a <= b", a <= b)  # a <= b True

a = 'Python'
b = 'python'
print("a > b", a > b)  # a > b False
print("a >= b", a >= b)  # a >= b False
print("a < b", a < b)  # a < b True
print("a <= b", a <= b)  # a <= b True

a = True
b = False
print("a > b", a > b)  # a > b False
print("a >= b", a >= b)  # a >= b False
print("a < b", a < b)  # a < b True
print("a <= b", a <= b)  # a <= b True

# Chaining of Relational Operators.
# If all the condition is true then result is true and
# if any the condition is false then result is false
if 10 < 20 < 30 < 40:
    print("1. All Condition Passed.")

if 10 < 20 < 35 > 20:
    print("2. All Condition Passed.")

if 10 > 20 > 5 < 2:
    print("3. All Condition Passed.")
else:
    print("3. One condition failed")

# NOTE : == and != operators never raise any Error even for Complex Type.
# NOTE : For == and != operators, both the operands must be of compatible type.
print('Python' == 'Python')  # True
print(True == 10)  # False
print(True != 10)  # True
print(True == 1) # True
print(10==3+7==5*2==15-5) # True
print(1==2==3==4) # False
print('a' == 97) # False
print(10 == 10.0) # True

print("--- Logical Operators Demo ---")
# FOR BOOLEAN TYPE
# If we apply and,or,not operators on boolean types result is always boolean.
print(True and True) # True
print(True and False) # False
print(True or False) # True
print(not(False)) # True

# FOR NON BOOLEAN TYPES
# Empty String is treated as False
# 0 -> False
# Non-zero -> True

# AND Operator.
# Example: x and y
# if x evaluate to False then return x else return y.
print(10 and 20) # 20
print(0 and 12) # 0

# OR Operator.
# Example : x or y
# if x evaluate to True then return x else return y.
print(10 or 20) # 10
print(0 or 25) # 25
print(0 or 0) # 0
print(10 or 10/0) # 10

print(not 10) # False
print(not '') # True
print(not 0) # True