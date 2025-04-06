from math import factorial
n = int(input("N = "))

# Vẽ tam giác pascal:
for i in range(n):
    for j in range(n-i+1):
        print(end=" ") #In khoảng trống bên trái
 
    for j in range(i+1):
        # Dùng công thức: nCr = n!/((n-r)!*r!)
        # Mỗi phần tử của tam giác là kết quả của phép tính trên:
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    
    print() #Xuống dòng sau khi in xong 1 hàng