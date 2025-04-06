s = input("Nhập các số: ")

# Tạo tập hợp các số:
number_set = set(int(x) for x in s.split())

print("Tập hợp các số:",number_set)

# Số phần tử của tập:
print("Số phần tử của tập:",len(number_set))

# Phần tử lớn nhất trong tập:
print("Phần tử lớn nhất trong tập:",max(number_set))

# Phần tử nhỏ nhất trong tập:
print("Phần tử nhỏ nhất trong tập:",min(number_set))