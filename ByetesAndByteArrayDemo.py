# Reference : Durga Software Solutions.

# If user want to hold group of byte data types then use bytes.
# bytes values must be in range from 0 to 256.
# bytes data types are immutable.
# If we try to reassign b[0] = 21 results into error : TypeError: 'bytes' object does not support item assignment

# bytes demo

# If we give below values > 256 in bytes then following error occurs.
# ValueError: bytes must be in range(0, 256)
# x = [100,200,300,400]
x = [10,20,30,40]
b = bytes(x)
# b[0] = 21
print(type(b))
print(type(x))

# Access the values in bytes b
print(b[0])
# 10
print(b[1])
# 20
print(b[-1])
# 40
print(b[0:3])
# b'\n\x14\x1e'
for x in b : print(x)
# 10
# 20
# 30
# 40

# If user want to hold group of byte data types then use bytes.
# Both bytes and bytearray are same, ONLY DIFFERENCE IS 'bytearray' IS MUTABLE.

a = [10,20,30,40]
byte_array = bytearray(a)
print(type(byte_array))
# <class 'bytearray'>
for i in byte_array:print(i)
# 10
# 20
# 30
# 40
byte_array[0] = 100
for i in byte_array:print(i)
# 100
# 20
# 30
# 40