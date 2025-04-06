def tam_giac(a,b,c):
    if (a+b<=c or a+c<=b or b+c<=a):
        return False
    return True
try:
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    if a<=0 or b <=0 or c<=0:
        raise Exception("Phải nhập số dương!")
    if not tam_giac(a,b,c):
        raise Exception("Không phải 3 cạnh của tam giác")
except ValueError:
    print("Phải nhập vào số!")
except Exception as x:
    print("Lỗi:",x)
    

