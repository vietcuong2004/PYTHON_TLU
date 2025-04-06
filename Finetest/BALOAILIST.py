N = int(input("Nhap N: "))
list_A = []
list_B = []
list_C = []

for i in range(N):
    x = input("Nhap gia tri thu %d: "%(i+1))
    try:
        x = int(x)
        list_A.append(x)
    except ValueError:
        try:
            x = float(x)
            list_B.append(x)
        except ValueError:
            list_C.append(x)
# Hàm sort: sắp xếp tăng dần:
list_A.sort(reverse=True)
list_B.sort(reverse=True)
list_C.sort(reverse=True)

print("A =", list_A)
print("B =", list_B)
print("C =", list_C)