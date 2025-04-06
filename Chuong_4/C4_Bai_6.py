# Hàm tìm ra các chữ cái xuất hiện trong chuỗi:
def Letter(string):
	# Tạo mảng để lưu các chữ cái:
	Array = []
	for x in string:
		if (x.isalpha() == True) and (x not in Array):
			Array.append(x)
	Array.sort()
	return Array

# Hàm đếm số lần xuất hiện của 1 chữ cái trong chuỗi
def Count_Letter(string,letter):
	count = string.count(letter)
	return count


s = input("Nhập chuỗi: ")
# In ra các chữ cái xuất hiện trong chuỗi:
result = Letter(s)
print(">> Các chữ cái có trong chuỗi:",result)

# In ra tần suất xuất hiện
for x in result:
	count = Count_Letter(s,x)
	print(">> Chữ cái '%s' xuất hiện %d lần." %(x,count))