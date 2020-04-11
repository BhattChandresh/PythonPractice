#input: B4A1D3
#output: ABD134

s=input("Enter String:")
digit = char = result=''
char = ''
for x in s:
    if x.isalpha():
        char = char + x
    elif x.isdigit():
        digit = digit +x
print(char)
print(digit)
for x in sorted(char):
    result = result + x
for x in sorted(digit):
    result = result + x
print("Result : ", result)