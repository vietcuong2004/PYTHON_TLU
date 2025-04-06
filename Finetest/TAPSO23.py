n = int(input("N = "))
# Tạo mảng gồm n phần tử đã được gán sẵn giá trị bằng 1
# Thực hiện tính toán các số được thêm vào dần dần từ phần tử thứ 2:
A = [1]*n

# Tạo 2 con trỏ:
k2 = 0
k3 = 0

# Tính toán:
for i in range(1,n):
	T2 = 2*A[k2] + 1
	T3 = 3*A[k3] + 1
	A[i] = min(T2,T3)
	if (A[i] == T2): k2 += 1
	if (A[i] == T3): k3 += 1
print("%d so dau tien cua N23:" %n,*A)