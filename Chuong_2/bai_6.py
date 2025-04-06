def giai_thua(n):
    gt=1
    for i in range(1,n+1):
        gt=gt*i
    return gt
n = int(input("N = "))
Fn=0
for j in range(1,n+1):
    Fn = Fn+giai_thua(j)
print("F(n) =",Fn)