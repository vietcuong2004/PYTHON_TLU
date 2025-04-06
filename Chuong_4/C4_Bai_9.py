s = input("Nhập chuỗi S: ")

# Cách 1: Tạo ra chuỗi đảo ngược của s
# Reverse = "".join(s[len(s)::-1])
#if(Reverse == s):

# Cách 2: làm trực tiếp, lấy phần tử của S từ cuối lên đầu, so sánh với S:
if (s == s[len(s)::-1]):
	print(">> S là chuỗi đối xứng.")
else:
	print(">> S không phải chuỗi đối xứng.")