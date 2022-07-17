hour,minute=map(int,input().split(' '))
need=int(input())
minute+=need
while True:
    if minute>=60:
        minute-=60
        hour+=1
        if hour>=24:
            hour-=24
    else:
        break
print(hour,minute)