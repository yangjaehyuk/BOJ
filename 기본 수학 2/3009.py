_1=list(input().split(' '))
_2=list(input().split(' '))
_3=list(input().split(' '))
for _ in range(3):
    max_x=max(_1[0],_2[0],_3[0])
    max_y=max(_1[1],_2[1],_3[1])
    min_x=min(_1[0],_2[0],_3[0])
    min_y=min(_1[1],_2[1],_3[1])
if not ((_1[0] and _2[0] and _3[0]).count(max_x)==2 or (_1[0] and _2[0] and _3[0]).count(min_x)==2):
    if not((_1[0]+_2[0]+_3[0]).count(max_x)==2):
        print(max_x, end=" ")
    elif not((_1[0]+_2[0]+_3[0]).count(min_x) == 2):
        print(min_x, end=" ")
if not ((_1[1] and _2[1] and _3[1]).count(max_y)==2 or (_1[1] and _2[1] and _3[1]).count(min_y)==2):
    if not ((_1[1]+_2[1]+_3[1]).count(max_y) == 2):
        print(max_y, end=" ")
    elif not((_1[1]+_2[1]+_3[1]).count(min_y) == 2):
        print(min_y, end=" ")