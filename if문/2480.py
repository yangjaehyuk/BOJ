dice=list(map(int,input().split(' ')))
dice1=dice[0]
dice2=dice[1]
dice3=dice[2]
rst=0
if dice1==dice2==dice3:
    rst+=10000+dice1*1000
elif dice1==dice2 or dice1==dice3 or dice2==dice3:
    if dice1==dice2 and (dice1!=dice3 or dice2!=dice3):
        rst+=1000+dice1*100
    elif dice1==dice3 and (dice1!=dice2 or dice2!=dice3):
        rst+=1000+dice1*100
    elif dice2==dice3 and (dice1!=dice2 or dice1!=dice3):
        rst+=1000+dice2*100
else:
    rst+=max(dice)*100
print(rst)