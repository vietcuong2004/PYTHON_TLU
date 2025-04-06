import datetime
d=int(input("Nhap ngay d = "))
m=int(input("Nhap thang m = "))
y=int(input("Nhap nam y = "))
k=int(input("Nhap so ngay k= "))
now=datetime.datetime(y,m,d)
result=now+datetime.timedelta(days=k)
print(k,"ngày tiếp theo là ngày:",result.strftime("%d/%m/%Y"))