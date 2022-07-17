a=list(map(int,input().split(' ')))
new_a=sorted(a,reverse=True)
new1_a=sorted(a,reverse=False)
if(a==new_a):
    b='descending'
elif(a==new1_a):
    b='ascending'
else:
    b='mixed'
print(b)