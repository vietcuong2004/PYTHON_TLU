# Nhập 3 số nguyên A, B và C
A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

# Tạo một list chứa 3 số
Array = [A, B, C]

# Sắp xếp list theo thứ tự tăng dần
Array.sort()

# In ra các số theo thứ tự tăng dần, không in lặp các giá trị giống nhau
print("Xep tang dan:",end="")
previous_number = None
for number in Array:
    if number != previous_number:
        print(" ",number,sep="",end = "")
        previous_number = number
print()
