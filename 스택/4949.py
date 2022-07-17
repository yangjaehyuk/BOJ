while True:
    a=str(input()).rstrip()
    rst=[]
    if(a[0]==')' or a[0]==']'):
        print("no")
    elif(a[0]=='.'):
        break
    else:
        for j in range(len(a)):
            if(a[j]=='(' or a[j]==')' or a[j]=='[' or a[j]==']'):
                rst.append(a[j])
                if(len(rst)>2):
                    if(rst[-2]=='(' and rst[-1]==')'):
                        del rst[-2]
                        del rst[-1]
                    elif(rst[-2]=='[' and rst[-1]==']'):
                        del rst[-2]
                        del rst[-1]
                else:
                    if(len(rst)==2):
                        if(rst[0]=='(' and rst[1]==')'):
                            del rst[0]
                            del rst[0]
                        elif(rst[0]=='[' and rst[1]==']'):
                            del rst[0]
                            del rst[0]
                    elif(len(rst)<=1):
                        continue
        if(len(rst)==0):
            print("yes")
        else:
            print("no")