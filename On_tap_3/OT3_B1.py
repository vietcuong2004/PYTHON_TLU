def LapBacK(s,k):
	end = len(s) - k + 1
	for i in range(end):
		sub1 = s[i:i+k]
		sub2 = s[i+k:i+2*k]
		if sub1==sub2: return True
	return False

s = input("s = ")
k = int(input("k = "))
if LapBacK(s,k):
	print("Day lap bac",k)
else:
	print("Day khong lap.")