n = int(input("N = "))
# Chuyển 2 mũ n thành chuỗi kí tự để dễ dàng tìm được các chữ số
number_to_str = str(2**n)
tong =0
# Chuỗi cũng là 1 mảng => Mỗi kí tự của chuỗi là 1 chữ số của 2^n:
for i in number_to_str:
	tong += int(i) # Ép kiểu kí tự thành kiểu nguyên để tính tổng các chữ số
print("Tong =",tong)
