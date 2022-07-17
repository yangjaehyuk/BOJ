student_number=int(input())
while (student_number < 2 or student_number > 50):
    student_number = int(input())
student_list=[]
for i in range(student_number):
    w,h=map(int,input().split(' '))
    student_list.append((w,h))
for j in student_list:
    rank=1
    for k in student_list:
        if((j[0]<k[0]) and (j[1]<k[1])):
            rank+=1
        if(k[0]<10 or k[1]<10 or j[0]>200 or j[1]>200):
            exit()
    print(rank, end=" ")






