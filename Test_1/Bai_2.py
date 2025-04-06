s = input("Nhập họ tên đầy đủ:")
full_name = s.split()
ho = full_name[0]
ten_dem = " ".join(full_name[1:len(full_name)-1])
ten = full_name[-1]
print("Họ:",ho)
print("Đệm:",ten_dem)
print("Tên:",ten)