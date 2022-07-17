a=int(input())
if(a<1 or a>4000):
    exit()
if(a%4==0 and (a%100!=0 or a%400==0)):
    print('1')
if not(a%4==0 and (a%100!=0 or a%400==0)):
    print('0')
