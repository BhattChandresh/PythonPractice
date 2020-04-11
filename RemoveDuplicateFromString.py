# Reference : Durga Software Solutions.

# Method-1
s = input('Enter the String:')
result = ''
l = []
for i in s:
    if i not in l:
        l.append(i)
print(''.join(l))


# Method-2
print(''.join(set(s)))