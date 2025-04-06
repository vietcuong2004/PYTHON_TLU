n = int(input("Nhap N: "))
A =[]
B= []
for i in range(1,n+1):
	x = input("Nhap gia tri thu %d: " %i)
	try:
		x = int(x)
		A.append(x)
	except ValueError:
		try:
			x = float(x)
			A.append(x)
		except ValueError:
			B.append(x)
if(len(A)>0):
	print("TBC cua A =",sum(A)/len(A))
print("B =",B)