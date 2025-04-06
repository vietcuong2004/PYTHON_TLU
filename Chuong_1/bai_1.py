a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))
delta = b*b-4*a*c
if delta==0:
	print("Nghiem kep: x = ", str(-b/2/a))
if delta<0:
	print("Phuong trinh vo nghiem")
if delta>0:
	## print("X1 = " + str((-b+delta**0.5)/2/a))
	## print("X2 = " + str((-b-delta**0.5)/2/a))
	x1=(-b+delta**0.5)/(2*a)
	x2=(-b-delta**0.5)/(2*a)
	print("X1 = %f" %x1)
	print("X2 = %f" %x2)