a=[-5, 9, 0, 3, -1, -2, 1,4, -2, 10, 2, 0, -9, 8, 10, -9,0, -5, -5, 7]
min=int(input("минимум"))
max=int(input("максимум"))
b=[]
for i in range(0,len(a)):
    if a[i]>=min and max>=a[i]:
        b.append(i)
print(b)