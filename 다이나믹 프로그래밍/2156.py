n=int(input())
dp=[0]*n
drink=[]
for i in range(n):
    podo=int(input())
    drink.append(podo)
if n==1:
    print(drink[0])
elif n==2:
    print(drink[0]+drink[1])
else:
    dp[0]=drink[0]
    dp[1]=drink[0]+drink[1]
    dp[2]=max(dp[1],dp[0]+drink[2],drink[1]+drink[2])
    for j in range(3, n):
        dp[j] = max(dp[j-3]+drink[j-1]+drink[j],dp[j-2]+drink[j],dp[j-1])
    dp.sort(reverse=True)
    print(dp[0])