# Reference : Dugra Software Solutions.
# In Python there are two types of index are possible.
# positive index -> Left to right
#   s='Python'  [0=P,1=y,2=t,3=h,4=o,5=n]
# Negative index -> Right to left
#   s='Python'  [-1=n,-2=o,-3=h,-4=t,-5=y,-6=P]

s = 'Python'
print("Positive Index Demo")
for i in range(len(s)):
    print(s[i])
print("Negative Index Demo")
print(s[-1],s[-2],s[-3],s[-4],s[-5],s[-6])

# string[begin:end]  here end = end -1
# Example s[1:4] means returned substring is from 1 to (4-1) = 3

#slice[begin:end]
print("Basic Slice Demo")
print(s[1:4]) #yth
# If we do not specify end then by default end = last index of string.
print(s[0:]) #Python
# If we do not specify begin then by default begin = 0 index of string.
print(s[:4]) #Pyth
# If we do not specify begin then by default begin = 0 index of string.
# If we do not specify end then by default end = last index of string.
print(s[:]) #Python
# begin index must always be lower than the end index.
print(s[-1:-4]) #''
print(s[-4:-1]) #tho
# Slice operation never throws indexError.
# Here 100 is considered as end index of String
print(s[1:100]) #Python

#slice[begin:end:step]
s = "DurgaSoftwareSolutions"
print(s[1:10]) # urgaSoftw
print(s[1:10:2]) # ugSfw

# Repetation Operator
s = "Python "
print(s*10) # Python Python Python Python Python Python Python Python Python Python

# Find the Length of a String
print("Length of String :",len(s)) # Length of String : 7
