t=int(input())
for i in range(t):
    a, b = map(int, input().split(' '))
    if (a < 0 or a > 10 or b < 0 or b > 10):
        exit()
    result=a+b
    print(result)