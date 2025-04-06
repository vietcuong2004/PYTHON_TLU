A = list(map(int, input("Nhập dãy (phân cách bởi ','): ").split(',')))
KQ = []

while len(A) > 0:
    current = float('-inf') # current là một phần tử có giá trị âm vô cùng
    i = 0
    sub = []  # Tạo danh sách chứa chuỗi con
    while i < len(A):
    	# so sánh phần tử currrent với toàn bộ phần tử còn lại trong list A
		# nếu gặp phần tử nào lớn hơn current thì ta thêm vào chuỗi con sub
        if A[i] > current:
            current = A[i] 
            sub.append(A[i])
            del A[i]
        else:
            i += 1
    KQ.append(sub)  # Thêm danh sách con vào KQ

print("Kết quả sau khi xử lý: ",end = '')
for i,sub in enumerate(KQ):
	print(*sub,end = ' ')
	if i < len(KQ)-1:
		print('|',end = ' ')
