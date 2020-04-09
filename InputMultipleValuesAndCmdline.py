# Reference : Durga Software Solutions.

# Example that illustrate to enter multiple values with different data types from keyboard.

a,b,c = [eval(x) for x in input("Enter 3 values:").split(',')]
print(type(a))
print(type(b))
print(type(c))

from sys import argv
args = argv[1:] # This line do nothing.
print("Length of command line arguments : ",len(argv))
for x in argv :
    print(x)