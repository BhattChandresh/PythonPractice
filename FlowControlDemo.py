# Reference : Durga Software Solutions.

print("--- Conditional statements Demo ---")

# if and else example
x = int(input("Enter a number:"))
if x % 2 == 0 :
    print("%i is a Even number" %x)
else:
    print("%i is a Odd number" %x)

# if,elif and else example
x = input("Enter brand:")
if x == 'AAA':
    print('AAA is good choice')
    print("Go for it.")
elif x == 'BBB':
    print("BBB is excellent choice")
    print("Must go for it")
else:
    print("Bad choice")

print("--- Iterative statements Demo ---")
s = 'Chandresh Bhatt'
count = 0
for x in s:
    count += 1
    print(x)
print("Total Character in s :", count)

# Print the number 1 to 10 in descending order.
for x in range(10,0,-1):
    print(x)

# while loop demo.

t = int(input("Enter a number:"))
i = 1
sum = 0
while i <= t:
    sum = sum +i
    i +=1
print(sum)

n = int(input('Enter the number:'))
for i in range(n+1):
    print('* '* i)
'''
if n = 5
* 
* * 
* * * 
* * * * 
* * * * *
'''

n = int(input('Enter the number:'))
for i in range(n):
    print('* ' * n,end = " ""\n")
'''
if n=5
* * * * *  
* * * * *  
* * * * *  
* * * * *  
* * * * * 
'''

# else statement executed when loop is completed without
# executing break statement.
print("--- for else demo ---")
l = [10,20,60,70,80,90]
for item in l:
    if item > 500:
        print("Higher value item, Please visit another web page")
        break
    print(item)
else:
    print("Loop executed without break statement")


l = [10,20,60,700,70,80,90]
for item in l:
    if item > 500:
        print("Higher value item, Please visit another web page")
        break
    print(item)
else:
    print("Loop executed without break statement")


print("--- pass demo ---")
for i in range(100):
    if i%10 == 0:
        print(i)
    else:pass

print("--- del demo ---")
print("del is a keyword in Python")
x=10
print(x)
del x
# print(x) # This line produce an error if we try to access variable after deleting it :  NameError: name 'x' is not defined

