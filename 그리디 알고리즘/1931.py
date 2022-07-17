n=int(input())
schedule=[]
for i in range(n):
    schedule.append(list(map(int,input().split(' '))))
schedule.sort(key=lambda x:x[0])
schedule.sort(key=lambda x:x[1])
last=0
count=0
for s,e in schedule:
    if s>=last:
        count+=1
        last=e
print(count)