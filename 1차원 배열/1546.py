n=int(input())
result=list(map(int,input().split(' ')))
max=max(result)
fix_result=0
arr=[]
sum_result=[]
for i in range(0,len(result)):
    fix_result=float(result[i]/max*100)
    arr.append(fix_result)
sum_result=sum(arr)
avg_result=sum_result/n
print(avg_result)