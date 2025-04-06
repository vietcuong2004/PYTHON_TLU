def nhap(tb1,kieu_du_lieu,tb2):
	print(tb1)
	data = {}
	while True:
		ten_mat_hang = input("  Ten mat hang: ")
		if ten_mat_hang == "": 
			break
		data[ten_mat_hang] = kieu_du_lieu(input(tb2))
	return data

gia_ban = nhap("NHAP BANG GIA:",float,"  Gia ban hang: ")
hang_ton = nhap("NHAP HANG TON:",int,"  So luong ton kho: ")
L = [(w,0 if w not in hang_ton else gia_ban[w]*hang_ton[w]) for w in gia_ban]
L.sort(key = lambda x:(-x[1],x[0]))
chieu_rong = max([len(w[0]) for w in L])
print("THONG KE HANG TON:")
for w in L:
	print(" ",w[0].ljust(chieu_rong),"%6.2f" %w[1])