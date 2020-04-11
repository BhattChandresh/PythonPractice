# Reference : Durga Software Solutions.

s = input('Enter a String:')
d={}
for x in s:
    if x not in d:
        d[x] = 1
    else:
        d[x] = d[x] + 1
for k,v in d.items():
    print('{} Occurs {} times'.format(k,v))