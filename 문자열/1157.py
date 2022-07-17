word=list(input().upper())
a=[]
count={}
n=0
for i in range(0,len(word)):
    a.append(ord(word[i]))
for j in word:
    try: count[j]+=1
    except: count[j]=1
max(count,key=count.get)
if(len([k for k,v in count.items() if max(count.values())==v])>1):
    print("?")
else:
    max=0
    s1=set(word)
    for x in s1:
        current = word.count(x)
        if max < current:
            max = current
            a = []
            a.append(x)
        elif max == current:
            a.append(x)
    a.sort()
    print(''.join(a))