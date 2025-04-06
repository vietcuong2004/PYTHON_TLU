s = input("Nhập dãy các từ: ")

# Lưu các từ vào mảng Word:
Word = s.split()

# Tìm từ dài nhất:
Max = max(Word,key = len) # key = len: tìm max theo tiêu chí độ dài của chuỗi
						  # Còn có key = abs (Trị tuyệt đối), key = None (mặc định)

#Tìm các từ có cùng độ dài với từ dài nhất:
Same_len = []
for x in Word:
	if(len(x) == len(Max)):
		Same_len.append(x)

#In ra kết quả:
print(">> Từ dài nhất trong các từ trên:",Max)
print(">> Các từ có cùng độ dài max:",Same_len)

# In các từ trên cùng 1 dòng:
#for x in Same_len:
	#print (x,end = " ")