t=int(input())
for i in range(t):
    a=str(input()).rstrip()
    rst=[]
    if(a[0]==')'):
        print("NO")
    else:
        for j in range(len(a)):
            rst.append(a[j])
            if(len(rst)>2):
                if(rst[-2]=='(' and rst[-1]==')'):
                    del rst[-2]
                    del rst[-1]
            else:
                if(len(rst)==2):
                    if(rst[0]=='(' and rst[1]==')'):
                        del rst[0]
                        del rst[0]
                elif(len(rst)<=1):
                    continue
        if('(' in rst):
            print("NO")
        elif(')' in rst):
            print("NO")
        else:
            print("YES")