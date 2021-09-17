import re
import sys

# this line enables you to write multiple sentence like code snippet
lines = ''.join(sys.stdin.readlines())

if bool(re.search(r'(java|public static|System.out.println)',lines)):
        print("Java")
elif bool(re.search(r'(#include|printf)',lines)):
        print("C")
else:
    print("Python")



