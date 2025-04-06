string = input("Nhập các từ Tiếng Anh: ")
#Tách các từ:
s = string.split()

# Chuyển sang list để dùng hàm sắp xếp theo bảng chữ cái:
s = list(s)
s.sort(key = str.lower)

#In ra kết quả:
print("Các từ được sắp xếp theo bảng chữ cái:",s)