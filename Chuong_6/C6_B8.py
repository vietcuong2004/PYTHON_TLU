# Kiểm tra xem vé người chơi có trùng >=5 số so với vé trúng thưởng hay không
def kiem_tra(ve_nguoi_choi, ve_trung_thuong):
	# Chuyển danh sách về set để dùng phép giao
	# Dùng phép giao để xem bao nhiêu phần tử trùng:
	so_trung_nhau = set(ve_nguoi_choi) & set(ve_trung_thuong)
	if len(so_trung_nhau) >= 5:
		return True
	else: return False

# Nhập số người chơi:
n = int(input(">> Nhập số lượng người chơi: "))

# Tạo 1 list để lưu trữ vé của toàn bộ người chơi:
danh_sach_ve = []

# Nhập vé (các bộ số) của toàn bộ người chơi:
for i in range (n):
	print(">> Nhập bộ số của người chơi thứ %d (6 số): " %(i+1))
	ve_nguoi_choi = list(map(int,input().split()))
	# Thêm bộ số vừa nhập (là 1 list) vào danh sách vé:
	danh_sach_ve.append(ve_nguoi_choi)

# Nhập bộ số của giải đặc biệt:
print(">> Giải đặc biệt (6 số): ")
ve_trung_thuong = list(map(int,input().split()))

# Tìm người trúng thưởng và in ra bộ số của người trúng thưởng:
print(">> Danh sách trúng thưởng:")
for i,ve in enumerate(danh_sach_ve,start = 1):
	if kiem_tra(ve,ve_trung_thuong) == True:
		print(i,". Người chơi ",i,": ",ve,sep="")