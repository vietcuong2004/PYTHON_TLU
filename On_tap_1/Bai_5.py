s = input("Nhập chuỗi các số, cách nhau bởi dấu ',': ")
A = [int(x) for x in s.split(',')]
tong_binh_phuong = sum(x**2 for x in A)
binh_phuong_tong = (sum(A))**2
# print(tong_binh_phuong)
# print(binh_phuong_tong)
print("Chênh lệch:",binh_phuong_tong-tong_binh_phuong)
