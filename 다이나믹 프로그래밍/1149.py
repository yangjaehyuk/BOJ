import sys
n=int(sys.stdin.readline())
home=[]
for i in range(n):
    home.append(list(map(int,sys.stdin.readline().split(' '))))
for j in range(1,n):
    home[j][0]=min(home[j-1][1],home[j-1][2])+home[j][0]
    home[j][1]=min(home[j-1][0],home[j-1][2])+home[j][1]
    home[j][2]=min(home[j-1][0],home[j-1][1])+home[j][2]
print(min(home[n-1]))