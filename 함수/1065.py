list_n=str(input())
count=0
for i in range(1,int(list_n)+1):
    su = list(map(int, str(i)))
    if (len(su) <= 2):
        count += 1
    else:
        su = list(map(int, str(i)))
        if(su[0]-su[1]==su[1]-su[2]):
            count+=1
print(count)
