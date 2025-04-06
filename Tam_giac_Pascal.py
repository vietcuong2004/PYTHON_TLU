from math import *
def C(k,n):
	return factorial(n)//(factorial(k)*factorial(n-k))
	
n = int(input("N = "))
for i in range(0,n): # Hệ số mỗi hàng là tất cả các tổ hợp của i
					 # Với i chạy từ 0 đến n-1
	print((n-i-1)*' ',end='')
	for j in range(0,i+1): 
		print(C(j,i),end=' ');
	print()