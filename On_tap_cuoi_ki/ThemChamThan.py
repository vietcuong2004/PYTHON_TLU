s = input("Nhap S: ")
count = s.count('!')
if count==0:
	s += "!!"
elif count%2 != 0:
	s += "!"
print("Chuoi S sau khi xu ly:",s)