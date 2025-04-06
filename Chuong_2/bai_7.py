# Nhập điểm hợp lệ:
while True:
	diem = float(input("Nhập điểm của sinh viên: "))
	if (diem in range(0,10)):
		break
	else:
		print("Nhập sai, điểm nằm trong khoảng [0,10].")
# Xếp loại sinh viên:		
if (diem < 3.5):
	print("Xếp loại yếu")
elif (diem >= 3.5) and (diem < 5):
	print("Xếp loại kém")
elif (diem >= 5) and (diem < 6.5):
	print("Xếp loại trung bình")
elif (diem >= 6.5) and (diem < 8):
	print("Xếp loại khá")
elif (diem >= 8) and (diem < 9):
	print("Xếp loại giỏi")
else:
	print("Xếp loại xuất sắc")