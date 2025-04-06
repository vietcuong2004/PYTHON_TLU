from math import sqrt
N = int(input("N = "))
f = 0
for i in range (1,N+1):
	f += sqrt((i*(i+1))/2)

print("F(%d) = %.7f"%(N,f))