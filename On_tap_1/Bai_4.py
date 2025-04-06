def dx(n):
	return str(n)==str(n)[::-1]
def dxlonnhat(n):
    for i in range(n - 1, 0 , -1):
        if dx(i):
            return i
n=int(input("N = "))
print("Đối xứng lớn nhất nhỏ hơn N:", dxlonnhat(n)) 
