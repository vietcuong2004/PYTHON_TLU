a = list(map(int,input("Nhập dãy số phân cách bởi dấu ',': ").split(',')))
chan = []
le = []
for x in a:
	if (x%2 == 0):
		chan.append(x)
	else:
		le.append(x)

# Ghép 2 mảng thành kết quả:
kq = sorted(chan,reverse = True) + sorted(le)
print(kq)