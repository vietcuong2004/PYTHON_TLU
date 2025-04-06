def total(n):
	tong=0
	while (n>0):
		tong = tong + n%10 #chia lấy dư, cộng số ở hàng đơn vị vào tổng đầu tiên
		                   #sau đó mới cộng đến các số ở hàng chục, trăm ...
		n = n//10 #chia lấy nguyên
	return tong
n = int(input("Nhập vào số nguyên N = "))
print("Tổng các chữ số của N = ",total(n))
