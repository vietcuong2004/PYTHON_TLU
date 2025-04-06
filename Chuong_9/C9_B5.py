f = open("Test.txt",encoding = 'utf-8')
s = f.read()
# Chuyển đổi toàn bộ file thành chữ thường:
# s = s.lower()
# Lấy tập hợp các chữ cái có trong file:
alpha = set(s)
alpha_count = {} #Từ điển lưu trữ các chữ cái và số lần xuất hiện
# Đếm số lần xuất hiện của các chữ cái:
for x in alpha:
	if x.isalpha():
		count = s.count(x)
		alpha_count[x] = count 
print(alpha_count)