try:
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))
    if b == 0:
        raise Exception("b không thể bằng 0")
    print("Phân số a/b = ",a / b)    
except ValueError:
    print("Lỗi: a hoặc b không phải là số nguyên")
except Exception as e:
    print("Lỗi:",e)
