n = int(input("Nhap N: "))
A = []
B = []
for i in range(1,n+1):
	x = input("Nhap gia tri thu %d: "%i)
	try:
		x = int(x)
		A.append(x)
	except ValueError:
		try: 
			x = float(x)
			A.append(x)
		except ValueError:
			B.append(x)
print("Tong cac phan tu cua A =",sum(A))
print("B = ",end='')
print(*B,sep='-')