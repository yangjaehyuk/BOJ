e,s,m=map(int,input().split(' '))
'''e<16,s<29,m<20'''
e1=s1=m1=0
count=0
while True:
    if e==e1 and s==s1 and m==m1:
        print(count)
        break
    else:
        e1+=1
        s1+=1
        m1+=1
        count+=1
        if e1==16:
            e1=1
        if s1==29:
            s1=1
        if m1==20:
            m1=1