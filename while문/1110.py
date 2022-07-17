n=str(input())
result=list(map(int,str(n)))
real_result=0
count=0
while True:
    if (len(result) != 2):
        result.append(0)
        n=n+'0'
    real_result = sum(result)%10
    new_number = str(result[1]) + str(real_result)
    result=list(map(int, str(new_number)))
    count+=1
    if (int(n) == int(new_number)):
        break

print(count)



