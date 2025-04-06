def Tong_Uoc_So (n):
	tong = 0
	for i in range(2,int(n/2)+1):
		if (n%i == 0):
			tong += i
	return tong

n = int(input("N = "))
print(">> Các số nguyên dương nhỏ hơn %d có tổng các ước số thực sự lớn hơn chính nó:" %n)
for i in range(1,n):
	if Tong_Uoc_So(i)>i:
		print(" ",i,sep = "",end = "")