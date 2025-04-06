from math import *
A = [] # khởi tạo mảng A để lưu trữ các số dương
print(">> Nhập vào các số dương:")
while True:
	n = int(input("+ N = "))
	if (n>0): # Không có điều kiện này thì mảng A sẽ nhận cả giá trị âm cuối cùng mà ta nhập
		A.append(n) # Thêm phần tử n vào mảng A
	if (n<=0):
		break
print(">> Đã nhập vào số âm, kết thúc nhập!")
UCLN = A[0]
BCNN = A[0]
if (len(A) < 2):
	print(">> Không đủ dữ liệu để tìm UCLN và BCNN!")
else:
	for x in A:
		UCLN = gcd(UCLN,x)
		BCNN = lcm(BCNN,x)
	print(">> Ước chung lớn nhất của các số dương vừa nhập là:",UCLN)
	print(">> Bội chung nhỏ nhất của các số dương vừa nhập là:",BCNN)
