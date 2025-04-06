n = int(input(">> Nhập vào số nguyên N: "))
print(">> N = %s trong hệ cơ số 16" %hex(n))
print(">> N = %s trong hệ cơ số 8" %oct(n))
print(">> N = %s trong hệ cơ số 2" %bin(n))

## Chuyển đổi cơ số mà không có các ký tự 0x,0o,0b... ở đầu:
##print(">> N = %s trong hệ cơ số 16" %hex(n)[2:])
##print(">> N = %s trong hệ cơ số 8" %oct(n)[2:])
##print(">> N = %s trong hệ cơ số 2" %bin(n)[2:])