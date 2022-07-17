t=int(input())
for i in range(t):
    n,s=input().split(' ')
    result=''
    for j in s:
        result+=int(n)*j
    print(result)
