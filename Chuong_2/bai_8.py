a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
# Tìm max: dùng hàm max
max_value = max(a,b,c)
print("Giá trị lớn nhất trong 3 số là:",max_value, sep = "",end = "\n")

# Tìm giá trị còn lại nếu có ít nhất 2 số cùng nhận giá trị lớn nhất:
if (a == max_value) and (b == max_value):
	print("Giá trị thứ ba cần tìm là",c)
elif (b == max_value) and (c == max_value):
	print("Giá trị thứ ba cần tìm là",a)
elif (a == max_value) and (c == max_value):
	print("Giá trị thứ ba cần tìm là",b)
else:
	print("Không có giá trị thỏa mãn")
	 