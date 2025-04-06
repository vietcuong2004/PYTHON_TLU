n = int(input("Nhập số nguyên n: "))
list_fibo = [0]
for i in range(0,n):
	a,b = 0,1
	while(b<n):
		a,b=b,a+b
		if(i==a):
			list_fibo.append(i)
print("List cac so fibo nho hon n: ",list_fibo)