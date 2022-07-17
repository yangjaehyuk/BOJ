import sys
item,weight=map(int,sys.stdin.readline().split(' '))
thing=[[0,0]]
knapsack=[[0 for _ in range(weight+1)] for _ in range(item+1)]
for i in range(item):
    thing.append(list(map(int,sys.stdin.readline().split(' '))))
for i in range(1,item+1):
    for j in range(1,weight+1):
        w=thing[i][0]
        v=thing[i][1]
        if w>j:
            """w가 최대 허융 무게인 j를 넘는 경우"""
            knapsack[i][j]=knapsack[i-1][j]
        else:
            knapsack[i][j]=max(knapsack[i-1][j],knapsack[i-1][j-w]+v)
print(knapsack[item][weight])