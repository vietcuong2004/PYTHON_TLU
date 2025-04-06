full_name = str(input("Nhập họ tên: "))

# Tách chuỗi vừa nhập thành các chuỗi con, mỗi từ là 1 phần tử, thêm các phần tử đó vào mảng split
split = full_name.split() 

# Họ là phần tử đầu tiên của chuỗi split:
first_name = split[0];

# Tên thật là các phần tử còn lại, dùng join để ghép các phần tử đó thành chuỗi duy nhất:
# Ghép các phần tử từ phần tử thứ 1 cho đến hết list split thành 1 chuỗi, mỗi phần tử cách nhau 1 dấu cách
last_name = " ".join(split[1:]) 

# In ra kết quả:
print(">> Họ của bạn:",first_name)
print(">> Tên của bạn:",last_name)