hamburger=[]
beverage=[]
for i in range(3):
    a=int(input())
    hamburger.append(a)
h_m=min(hamburger)
for j in range(2):
    b=int(input())
    beverage.append(b)
b_m=min(beverage)
print(h_m+b_m-50)