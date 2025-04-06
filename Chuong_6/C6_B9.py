# a) Nhập dữ liệu
print("a)")
nhan_su = set(int(x) for x in input("Mã nv phòng nhân sự (cách nhau bởi ','): ").split(','))
hanh_chinh = set(int(x) for x in input("Mã nv phòng hành chính (cách nhau bởi ','): ").split(',')) 
truyen_thong = set(int(x) for x in input("Mã nv phòng truyền thống (cách nhau bởi ','): ").split(',')) 

# b) Số nhân viên của 3 phòng:
print("\nb)")
print("Tổng số nhân viên:",len(nhan_su | hanh_chinh | truyen_thong)) # Dùng phép hợp 
print("Danh sách nhân viên phòng nhân sự:",nhan_su)
print("Danh sách nhân viên phòng hành chính:",hanh_chinh)
print("Danh sách nhân viên phòng truyền thông:",truyen_thong)

# c) Danh sách nhân viên thuộc cả 3 phòng:
print("\nc)")
A = truyen_thong & hanh_chinh & nhan_su
print("Danh sách nhân viên thuộc cả 3 phòng:",A if len(A)>0 else "Không có")

# d) Danh sách nhân viên chỉ thuộc 1 phòng:
print("\nd)")
# Cách 1: Dùng phép loại và phép hợp:
# D = (truyen_thong^hanh_chinh) | (hanh_chinh^nhan_su) | (truyen_thong^nhan_su)

# Cách 2: Dùng giao và hiệu (Có thể lấy kết quả để tính câu e):
B = hanh_chinh & nhan_su
C = hanh_chinh & truyen_thong
D = truyen_thong & nhan_su
E = (truyen_thong | hanh_chinh | nhan_su) - B - C - D
print("Danh sách nhân viên chỉ thuộc 1 phòng:",E if len(E) > 0 else "Không có") 

# e) Cặp phòng dùng chung nhiều nhân viên nhất:
print("\ne)")
max_nv = max(len(B),len(C),len(D))
if max_nv==0:
	print("Không có phòng nào dùng chung nhân viên")
else:
	print("Cặp phòng dùng chung nhiều nhân viên nhất:")
	if(max_nv == len(B)):
		print(">> (hành chính & nhân sự): %d nhân viên" %max_nv)
	if(max_nv == len(C)):
		print(">> (hành chính & truyền thông): %d nhân viên" %max_nv)
	if(max_nv == len(D)):
		print(">> (truyền thông & nhân sự): %d nhân viên" %max_nv)

# f) Mã nhân viên đầu tiên của phòng:
print("\nf)")
print("Nhân viên đầu tiên của phòng hành chính:",min(hanh_chinh))
print("Nhân viên đầu tiên của phòng nhân sự:",min(nhan_su))
print("Nhân viên đầu tiên của phòng truyền thông:",min(truyen_thong))