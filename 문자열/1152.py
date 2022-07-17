word=list(map(str,input().split(' ')))
count=0
word=list(filter(None,word))
for i in range(0,len(word)):
    count+=1
print(count)