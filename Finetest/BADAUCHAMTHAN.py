S = input("Nhap chuoi: ")
#while len(S)<3 or S[-3:] != "!!!":
while not (S.endswith("!!!")):
	S += "!"
print("Chuoi sau khi bo sung dau cham than: '%s'" %S)