from math import *
def isPrime1(n):
	i = 2
	while (i<=int(sqrt(n))):
		if (n % i == 0):
			return False
		else:
			i = i+1
	return True

def isPrime2(n):
	for i in range(2,int(sqrt(n))+1):
		if (n % i == 0): 
			return False
		else:
			continue
	return True

n = int(input("N = "))
if(isPrime2(n)):
	print("N là số nguyên tố")
else:
	print("N không là số nguyên tố")