def fibo(n,k):
	if (n<k):
		return n
	else:
		sum =0
		for i in range(1,k+1):
			sum += fibo(n-i,k)
		return sum

n = int(input("n = "))
k = int(input("k = "))
print(">> Fibo(n,k) =", fibo(n,k))