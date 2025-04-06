def isFibo(n):
	if (n==0) or (n==1):
		return True
	else: 
		return isFibo(n-1) + isFibo(n-2)

n = int(input("Nhập số nguyên N = "))
if (isFibo(n)):
	print("N là số Fibonacci")
else: 
	print("N không là số Fibonacci")