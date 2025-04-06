a = input("Nhập dãy số (phân cách bởi ';'): ")

# Tạo set các số vừa nhập:
s1 = list(map(int,a.split(';')))

# Tạo set các số từ 1 đến n:
n = len(s1)
s2 = set(x for x in range (1,n+1))

# In ra kết quả:
if set(s1) == s2:
	print("Có là dãy hoán vị")
else:
	print("Không là dãy hoán vị")