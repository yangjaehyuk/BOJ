import sys
import math
a=list(map(int,sys.stdin.readline().rstrip().split(' ')))
rst=(a[2]-a[1])/(a[0]-a[1])
print(math.ceil(rst))