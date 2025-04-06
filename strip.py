s = input("Nhập chuỗi: ")
print("Căn giữa chuỗi:",s.center(30,'+'))

#loại bỏ các dấu chấm than ở đầu và cuối chuỗi:
print("Cắt bỏ dấu chấm than ở đầu và cuối chuỗi:",s.strip('!'))
print("Cắt bỏ dấu chấm than ở cuối:",s.rstrip('!'))
print("Cắt bỏ dấu chấm than ở đầu:",s.lstrip('!'))