from math import sqrt
n = int(input("N = "))
m = int(n/2)+1
# Cho i chạy đến n//2 để giảm thời gian chạy
# => Sẽ thiếu ước là N
# => Thêm N vào set
s = set(i for i in range(1,m) if n%i==0)
s.add(n)
print("Tập các ước số của n:",s)