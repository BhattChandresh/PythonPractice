# Reference : Durga Software Solutions.

'''
Theory:
There are two ways to access string by character.
1. By using index
2. By using slice operator.
Please refer SliceOperatorDemo.py for more details.
'''

print("1. String Access by index")
s = input('Enter String:') # Example 0123456789
i =0
for x in s:
    print("Character present at positive index:{} and at negative index:{} is : {}".format(i,i-len(s),x))
    i +=1

print("2. String Access by slice operator")
#[begin:end:step]
# If step value is +ve then move forward (Left to Right) i.e. begin to end-1
# If step value is -ve then move backward (Right to Left) i.e begin to end+1
# In forward direction:
    # default value for begin index= 0
    # default value for end index = (length of string)-1
    # default value for step = 1
# In backword direction:
    # default value for begin index= -1
    # default value for end index = (length of string)+1
    # default value for step = -1

print(s[0:7:1]) #0123456
print(s[0:7:2]) #0246
print(s[0:7]) #0123456
print(s[0:]) #0123456789
print(s[::]) #0123456789
print(s[::-1]) #9876543210
print(s[2:8:-1])
#print(s[2:8:0]) # ValueError: slice step cannot be zero
print(s[-1:-6:-1]) #98765
print(s[2:-5:1]) #234
print(s[:0:-1]) #987654321
#print(s[2:-1:-1]) here end index = 0 Need to check that.


# We can apply + and * operator to String.
# + concatenation operator for which both operands must be string.
# * is String repetition operator for which one operand must be string and second one must be integer.
print('Python ' + '3.0')
print('Python ' *3)
print(4 * 'Practice ')

# Find the Length of a String
s = "Python "
print("Length of String :",len(s)) # Length of String : 7

# trim() equivalent method in Python is strip()
# trim() in Java = strip() in Python
# ltrim() in Java = lstrip() in Python
# rtrim() in Java = rstrip() in Python

s = '  Ahmedabad '
print(s.strip())
print(s.lstrip())
print(s.rstrip())


#find() -> returns the index of first match
#index() -> This method is same as find() method except
            # if substring is not found then it returns valueerror but find() returns -1
#rfind() -> returns the index of match from right side.
#rindex()

s = 'durgasoftdurgasoftdurgasoft'
print(s.find('soft')) #5
print(s.find('s')) #5
print(s.find('s',0,15)) #5
print(s.rfind('soft')) #23
print(s.find('the')) #-1
print(s.rfind('the')) #-1

#print(s.index('Zoo'))  #ValueError: substring not found

# replacment()
# replacment(oldstr,newstr)
s = "Learning Python is very difficult"
print("Original String:", s)
s = s.replace("difficult",'easy')
print("New String:", s)

#split()
#s.slipt(seperator) default seperator is space
#rsplit()
s = "Learning the Python"
l = s.split()
print(type(l))
for x in l:
    print(x)

s = "10,20,30,40,50,60,70,80"
print(s.split(',',3))
print(s.rsplit(',',3))

#join
l = ['aaa','bbbb','ccc']
s = '--'.join(l)
print(s) #aaa--bbbb--ccc

#upper()
#lower()
#swapcase()
#title()
#capitalize()

s ='learning python is very easy'
supper = s.upper()
print(supper) #LEARNING PYTHON IS VERY EASY
print(supper.lower()) #learning python is very easy
print(s.title()) #Learning Python Is Very Easy
print(s.capitalize()) #Learning python is very easy

s = 'AaBbCcdDeE'
print(s.swapcase()) #aAbBcCDdEe
