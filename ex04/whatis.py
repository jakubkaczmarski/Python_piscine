import sys

if sys.argv.__len__() == 1:
    exit(1)
if(sys.argv.__len__() != 2 ):
    print("AssertionError: More than one argument provided")
    exit(1)

num = 0
try:
    num = int(sys.argv[1])
except ValueError as err:
    print("AssertionError: argument is not an integer")
    exit(1)

if(not num % 2):
    print("I'm Even.")
else:
    print("I'm Odd")

    