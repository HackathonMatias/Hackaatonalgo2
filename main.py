# This program calculate the length of the hypotensive
# I never programing in Python sorry :(
import math
perimeter=1000
a=1
b=1
for a in range(1,perimeter):
    for b in range(a,perimeter):
        c=math.sqrt(pow(a,2)+pow(b,2))
        if c.is_integer() and (a+b+c)==perimeter:
            print('{'+str(a)+','+str(b)+','+str(int(c))+'}')

