x=int(input("Nhập vào số nguyên X = "))
count=1
while(x>9):
    #x=int(x/10)
    x=x//10 #chia lấy phần nguyên
    count += 1
print("X có %d chữ số" %count)
print("Chữ số đầu tiên của X là:",x)
