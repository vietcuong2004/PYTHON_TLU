n = int(input("N = "))
a,b = 0,1
while b <=n:
    a,b = b,a+b
print("Số Fibonacci lớn nhất nhỏ hơn %d:" %n,a)
