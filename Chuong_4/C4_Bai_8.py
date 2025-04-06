s = str(input("Nhập chuỗi: "))
for x in "0123456789":
    s = s.replace(x,"?")
print("Chuỗi sau khi xử lý:",s)