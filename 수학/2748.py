n=int(input())
rst=[0,1]
def f(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        for i in range(2,n+1):
            rst.append(rst[i-1]+rst[i-2])
    return rst
f(n)
print(rst[-1])