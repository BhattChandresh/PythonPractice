# Reference : Durga Software Solutions.

s = 'Learning Python is really easy'
# Method-1
print("Reverse String is :", s[::-1])

# Method-2
print("Reverse String is :", reversed(s))
for x in reversed(s):
    print(x,end='')

# Method-3
print()
print(''.join(reversed(s)))