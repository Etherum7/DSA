import os
c=0
for _,_, file in os.walk('/Users/krishnasmac/Downloads/Development/pyProjects/ALgorthims-DS/450DSA/practice'):
    print(file)
    c+=len(file)
print(c)