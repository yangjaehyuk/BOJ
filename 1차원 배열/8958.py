n=int(input())
result=0
result_list=[]
for i in range(n):
    result=list(input())
    sum_count = 0
    count = 0
    for j in result:
        if j == 'O':
            count+=1
            sum_count+=count
        else:
            count=0
    print(sum_count)