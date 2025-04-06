from math import sqrt
def tam_giac (a,b,c):
	if(a+b<=c or a+c<=b or c+b <=a or a<=0 or b<=0 or c<=0):
		return 0
	else:
		p = (a+b+c)/2
		s = sqrt(p*(p-a)*(p-b)*(p-c))
		return s
a = float(input("Do dai A = "))
b = float(input("Do dai B = "))
c = float(input("Do dai C = "))
d = float(input("Do dai D = "))
kq = tam_giac(a,b,c) + tam_giac(a,b,d) + tam_giac(b,c,d) + tam_giac(a,c,d)
print("Ket qua =", -1 if kq==0 else "%.5f" %kq)
