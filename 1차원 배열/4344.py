c=int(input())
for i in range(c):
    count=0
    d=list(input().split())
    e=list(map(int,d))
    sum_result=sum(e[1:])
    avg_result=sum_result/e[0]
    for j in e[1:]:
        if(j>avg_result):
            count+=1
    result=(count/e[0]*100)
    print('%.3f' %result + '%')

