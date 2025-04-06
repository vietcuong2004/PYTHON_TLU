#Kiểm tra năm nhuận:
def nam_nhuan(y):
	if (y%400 == 0) or ((y%4 == 0) and (y%100 != 0)):
		return 1
	else:
		return 0

# Số ngày trong tháng:
def so_ngay(days_of_month, month, year):
	# Tháng 4,6,9,11 có 30 ngày:
	if (month in [4,6,9,11]):
		days_of_month = 30
	# Tháng 1,3,5,7,10,12 có 31 ngày:
	elif(month in [1,3,5,7,10,12]):
		days_of_month = 31
	# Tháng 2:
	else:
		if (nam_nhuan(year) == 1):
			days_of_month = 29
		else:
			days_of_month = 28
	return days_of_month

# Kiểm tra xem ngày/tháng/năm nhập vào đã hợp lệ hay chưa (1 là hợp lệ, 0 là chưa hợp lệ):
def kiem_tra(d,m,y):
	# if not (d<0 or d>31 or m<0 or m>12 or y<0):
	# if (d>0 and d<=31 and m>0 and m<=12 and y>0):
	if ((d in range(1,31)) and (m in range(1,12)) and (y>0)):
		if(d > so_ngay(d,m,y)):
			return 0
		else:
			return 1
	else:
		return 0
		
# Tìm ngày hôm trước: 
def ngay_hom_truoc(d,m,y):
	d = d-1 
	if (d==0):
		# Nếu ngày giảm xuống = 0 thì ngày hiện tại đang là ngày đầu tiên của tháng đó
		# Suy ra ngày trước đó là ngày cuối cùng của tháng trước => giảm biến tháng xuống 1 đv
		# Tháng giảm xuống 0 => Giảm năm 1 đơn vị, ngày trước đó là ngày cuối cùng tháng trước
		m = m -1 
		if (m == 0):
			y = y-1
			m = 12
		d = so_ngay(d,m,y) 
	print("Ngày hôm trước là: %d/%d/%d" %(d,m,y))

# Tìm ngày hôm sau:
def ngay_hom_sau(d,m,y):
	d = d+1
	# Sau khi cộng, ngày d đã vượt quá số ngày của tháng đó
	# => Ngày mồng 1 của tháng tiếp theo:
	if (d > so_ngay(d,m,y)):
		d =1
		m = m+1 
		if (m >12):
			m = 1
			y = y+1
	print("Ngày hôm sau là: %d/%d/%d" %(d,m,y))		

# Nhập ngày tháng năm cho đến khi hợp lệ:
while True:
	d = int(input(">> Nhập vào ngày: "))
	m = int(input(">> Nhập vào tháng: "))
	y = int(input(">> Nhập vào năm: "))
	if kiem_tra(d,m,y) == 1:
		break
	else:
		print("Ngày,tháng,năm không hợp lệ!")
# In ra ngày tháng năm hiện tại:
print("Ngày/tháng/năm vừa nhập: %d/%d/%d"%(d,m,y))
# In ra ngày hôm trước:
ngay_hom_truoc(d,m,y)
# In ra ngày hôm sau:
ngay_hom_sau(d,m,y)