import math
def area2(xa,ya,xb,yb,xc,yc):
    AB = math.sqrt((xa-xb)*(xa-xb)+ (ya-yb)*(ya-yb))
    AC = math.sqrt((xa-xc)*(xa-xc)+ (ya-yb)*(ya-yb))
    BC = math.sqrt((xb-xc)*(xb-xc)+ (ya-yc)*(ya-yc))
    p=(AB+AC+BC)/2
    s = math.sqrt(p*(p-AB)*(p-AC)*(p-BC))
    return s
xa=float(input("xa = "))
ya=float(input("ya = "))
xb=float(input("xb = "))
yb=float(input("yb = "))
xc=float(input("xc = "))
yc=float(input("yc = "))
print("Diện tích tam giác = ",area2(xa,xb,ya,yb,xc,yc))
