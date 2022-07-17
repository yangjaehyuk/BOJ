import math
a=list(map(int,input().split(' ')))
d=[]
array = [True for i in range(a[1] + 1)]


for i in range(2, int(math.sqrt(a[1])) + 1):
    if array[i] == True:

        j = 2
        while i * j <= a[1]:
            array[i * j] = False
            j += 1


for i in range(a[0], a[1] + 1):
    if array[i]:
        d.append(i)
if 1 in d:
    d.remove(1)
for i in range(len(d)):
    print(d[i])