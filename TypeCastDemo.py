# Reference : Durga Software Solutions.
# Type casting in Python is also known as Type coersion

#   --- int() Demo ----
print(int(123.456))
# 123

print(int(True))
# 1

print(int(False))
# 0

# print(int(10+20j)) # Uncomment this line to execute this statement
# Error: TypeError: can't convert complex to int

# NOTE: If you want to convert string to int then string should always be
# decimal type, "int(OB1111)" will throw an error.

print(int("10"))
# 10

# print(int("OB1111")) # Uncomment this line to execute this statement
# ValueError: invalid literal for int() with base 10: 'OB1111'

#   --- float() Demo ---
print(float(20))
# 20.0

print(float(True))
# 1.0

print(float(False))
# 0.0

# print(float(12.3+45.6j)) # Uncomment this line to execute this statement
# TypeError: can't convert complex to float

print(float("10"))
# 10.0

print(float("10.7"))
# 10.7

# print(float("ten")) # # Uncomment this line to execute this statement
# ValueError: could not convert string to float: 'ten'

# NOTE: If you want to convert string to float then string should always be
# decimal type, "float(OB1111)" will throw an error.


# print(float("OB1111")) # Uncomment this line to execute this statement
# ValueError: could not convert string to float: 'OB1111'

# NOTE : Complex Type could not be cast to float, int in Python.

#   --- complex() Demo ---
# Form-1: complex(x) = x + 0j
# Form-2: complex(x,y) = x + yj
print(complex(5))
# (5+0j)
print(complex(10.5))
# (10.5+0j)
print(complex(True))
# (1+0j)
print(complex(False))
# 0j
print(complex("10"))
# (10+0j)
print(complex("10.5"))
# (10.5+0j)
# print(complex("ten")) # # Uncomment this line to execute this statement
# ValueError: complex() arg is a malformed string

# NOTE: If you want to convert string to float then string should always be
# decimal type, "float(OB1111)" will throw an error.

# print(complex("OB1111")) # Uncomment this line to execute this statement
# ValueError: complex() arg is a malformed string

print(complex(1,2))
# (1+2j)
print(complex(True,False))
# (1+0j)
print(complex(10,20.5))
# (10+20.5j)

# print(complex("5","7")) # Uncomment this line to execute this statement
# TypeError: complex() can't take second arg if first is a string

#   --- bool() Demo ---
# For int argument, 0 = False and Non-Zero = True.
print(bool(0))
# False
print(bool(11))
# True
print(bool(-12))
# True
# For float argument, 0.0 = False, for rest of the case is True.
print(bool(0.0))
# False
print(bool(0.01))
# True
print(bool(3.4))
# True
# For complex type argument, if both real,imaginary part are non zero = True.
# else False
print(bool(0+4.5j))
# True
print(bool(56+0j))
# True
print(bool(0+0j))
# False
# For string type argument, if string is empty ('') then False else True.
print(bool('Python'))
# True
print(bool(''))
# False
print(bool('  ')) # Here whitespace is also considered as one character so result = True.
# True

#   --- bool() Demo ---
print(str(30))
# 30
print(str(87.3))
# 87.3
print(str(True))
# True
print(str(False))
# False
print(str(30+56j))
# (30+56j)