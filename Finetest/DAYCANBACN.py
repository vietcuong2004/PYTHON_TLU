from math import *
n = int(input("N = "))
F = 0
for i in range(1,n+1):
	F += pow(i*(i+1)/2 , 1/i)
print("F(%d) = %.7f" %(n,F))