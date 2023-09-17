a=int(input("первый элемент прогрессии "))
rz=int(input("разность"))
l=int(input("количество чисел прогрессии"))
c=[]
c.append(a)
for i in range(1,l):
    c.append(c[i-1]+rz)
print(c)