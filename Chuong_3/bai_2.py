from math import *
def isPrime(n):
	for i in range(2,int(sqrt(n))+1):
		if (n % i == 0):
			return False
		else:
			continue
	return True

def PrintPrime(a,b):
	for i in range(a,b+1):
		if (isPrime(i)):
			print("%d" %i,end = " ")
		else:
			continue
a = int(input("A = "))
b = int(input("B = "))
print(">> Các số nguyên tố trong khoảng [%d,%d]: " %(a,b),end = '')
PrintPrime(a,b)