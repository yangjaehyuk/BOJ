b=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
a=list(input().upper())
count=2
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if(a[i] in b[j]):
            if (b.index(a[i]) < 3):
                count += 1
            elif (b.index(a[i]) < 6):
                count += 2
            elif (b.index(a[i]) < 9):
                count += 3
            elif (b.index(a[i]) < 12):
                count += 4
            elif (b.index(a[i]) < 15):
                count += 5
            elif (b.index(a[i]) < 19):
                count += 6
            elif (b.index(a[i]) < 22):
                count += 7
            elif (b.index(a[i]) < 26):
                count += 8
print(count+2*(len(a)-1))