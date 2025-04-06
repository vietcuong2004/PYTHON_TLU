def kiem_tra(s,k):
	t = len(s)-k+1
	for i in range(t):
		sub = s[i:i+k]
		sub1 = s[i+k:i+2*k]
		#if s.count(sub)>=2:
		if sub == sub1:
			return False
	return True

s = input("S = ")
k = int(input("k = "))
if kiem_tra(s,k):
	print("Day khong lap")
else:
	print("Day lap bac",k)