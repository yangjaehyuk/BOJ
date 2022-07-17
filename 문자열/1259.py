import sys
while True:
    a=sys.stdin.readline().rstrip()
    if(int(a)==0):
        exit()
    else:
        a=list(a)
        new_a=list(reversed(a))
        if(a==new_a):
            print('yes')
        else:
            print('no')