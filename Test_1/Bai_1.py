# thêm hàm factorial tính giai thừa trong thư viện math
from math import factorial
n = int(input("Nhập n = "))
f= 0
for i in range(1,n+1):
	f += 1/factorial(i)
print("F(N) = %.8f" %f)