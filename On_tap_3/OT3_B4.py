n = int(input("Số vi khuẩn ban đầu N = "))
h = int(input("Số giờ H = "))
for i in range(1,h+1):
	if i%2 == 0:
		n = 2*n
	else:
		n += min(int(n * 0.3), 30)  # Tăng tối đa 30% hoặc 30 vi khuẩn

print("Số vi khuẩn cuối cùng:",n)