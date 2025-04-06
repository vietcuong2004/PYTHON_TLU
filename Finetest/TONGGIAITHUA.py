#from math import factorial
n = int(input("Nhap N duong: "))
f = 0
gt = 1
for i in range(1,n+1):
    gt=gt*i
    f += gt
print("F(%d) = %d" %(n,f))