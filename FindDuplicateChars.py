# Reference : Durga Software Solutions.

#Method-1
s1 = input('Enter a String:')
s2 = input('Enter subString:')
flag = False
pos = -1
n = len(s1)
count = 0
while True:
    pos = s1.find(s2, pos + 1, n)
    if pos == -1:
        break
    print("Found at index : ", pos)
    count+= 1
    flag = True
if flag == False:
    print("Not Found")
print("No of occurance of substring :", count)

# Method-2
# count(string) method counting the number of substring in given string.
# syntax :
# 1. s.count(substring)
# 2. s.count(substring,begin,end)
s3 = 'ababababaaabbbb'
print(s3.count('ab')) #5