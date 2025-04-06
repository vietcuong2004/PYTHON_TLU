from math import sqrt
def tam_giac (a,b,c):
    if(a<=0 or b<=0 or c<=0):
        return -1
    elif(a+b<=c or a+c<=b or c+b <=a):
        return -1
    else:
        p = (a+b+c)/2
        s = sqrt(p*(p-a)*(p-b)*(p-c))
        return s
a = int(input("Do dai A = "))
b = int(input("Do dai B = "))
c = int(input("Do dai C = "))
d = int(input("Do dai D = "))
kq = max(tam_giac(a,b,c),tam_giac(a,b,d),tam_giac(b,c,d),tam_giac(a,c,d))
print("Ket qua =", -1 if kq==-1 else "%.5f" %kq)
