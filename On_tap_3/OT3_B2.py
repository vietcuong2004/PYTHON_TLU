def TimKQ(a,b):
	smallest = None
	for i in a:
		if i not in b:
			if smallest == None or i < smallest:
				smallest = i
	return smallest


a = list(map(int,input("A = ").split()))
b = list(map(int,input("B = ").split()))
kq = TimKQ(a,b)
if kq == None:
	print ("Không có")
else:
	vi_tri = len(a) - a[::-1].index(kq) - 1
	print("Vị trí xuất hiện cuối cùng:",vi_tri)