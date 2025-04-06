# Hàm gcd() nằm trong thư viện math dùng để tìm UCLN của 2 số:
from math import gcd
a = int(input("a = "))
b = int(input("b = "))

# Tập các ước chung của a và b là tập các ước của ước chung lớn nhất:
ucln = gcd(a,b)
m = ucln//2 +1
d = set(i for i in range(1,m) if ucln%i==0)

# Chỉ chạy đến m nên vẫn còn thiếu 1 ước là ucln(a,b):
d.add(ucln) 

# In kết quả:
print("Tập các ước số của %d và %d:" %(a,b), d)