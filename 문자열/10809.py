s=list(input())
k=[]
for i in range(0,len(s)):
    k.append(ord(s[i]))
for i in range(ord('a'),ord('z')+1):
    if (i not in k):
        print(-1, end=' ')
    else:
        print(k.index(i), end=' ')
