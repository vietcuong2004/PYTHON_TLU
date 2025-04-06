a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
s = {a,b,c} #Tạo set từ 3 số, nếu có 2 số trùng thì chỉ lấy 1 phần tử
if len(s)<=2 :
	print("BA SO KHONG PHAN BIET")
else:
	print("BA SO PHAN BIET")