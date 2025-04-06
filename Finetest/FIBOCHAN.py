def isFibo(n):
    if n < 0:
        return False
    a, b = 0, 1
    while b <= n:
    	if b == n:
    		return True
    	a, b = b, a + b
    return False
n = int(input("N = "))
if (isFibo(n) and n%2==0):
    print("N la so fibonacci chan")
else: 
    print("N khong phai la so fibonacci chan")