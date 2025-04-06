from math import sqrt
n = int(input("N = "))
s = 0
end = int(sqrt(n)) +1
for i in range(1,end):
	if (n%i == 0):
		j = n/i
		if(i==j):
			s += i
		else:
			s = s+i+j

print("Tong cac uoc so cua %d la %d" %(n,s))