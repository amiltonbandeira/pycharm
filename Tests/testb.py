import sys

print("arguments lists",sys.argv[0])
if len(sys.argv) > 1:
    print("Hello World " , sys.argv[1:])
if len(sys.argv) > 2:
    print("hello world b" ,sys.argv[2:])