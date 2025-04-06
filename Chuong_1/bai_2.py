tien=float(input("Số tiền gửi vào ngân hàng (triệu đồng): "))
#lai_suat=float(input("Lãi suất %/năm: "))
a= r'Lãi suất %/năm: '
lai_suat=float(input(a))
# Lãi suất sau 10 năm:
# Cách 1:
# print(">> Sau 10 năm bạn có %.2f triệu đồng."%float((tien*((1+lai_suat*0.01)**10))))

# Cách 2:
tien_1=tien
for i in range(0,10):
	tien_1 = tien_1*(1+lai_suat*0.01)
print(">>Sau 10 năm bạn có %.2f triệu đồng" %tien_1)

# Sau bao nhiêu năm bạn có ít nhất 50tr đồng ?
count=0
tien_2=tien
while(tien_2<=50):
	tien_2 = tien_2*(1+lai_suat*0.01)
	count += 1
print(">> Sau %d năm bạn có ít nhất 50tr đồng" %count)
