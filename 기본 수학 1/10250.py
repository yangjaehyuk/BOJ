import sys
n=int(sys.stdin.readline())
for _ in reversed(range(n)):
    a=list(map(int,sys.stdin.readline().split(' ')))
    b=0
    count=0
    ho=101
    r_ho=[]
    r_ho.append(ho)
    array=[[0 for col in range(a[1])] for row in range(a[0])]
    for i in range(a[0]*a[1]):
        if(a[0]>1):

            ho+=100
            r_ho.append(ho)
        else:
            ho+=1
            r_ho.append(ho)
        for j in range(len(array)):
            new_array=array[j][b]
            count+=1
            if(ho>=a[0]*100):
                ho=ho-((a[0]-1)*100)+1
                r_ho.append(ho)
    print(r_ho[a[2]-1])
