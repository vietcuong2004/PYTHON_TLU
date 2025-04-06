def F(N, memo):
    if N == 1:
        return 1

    if memo[N] != 0:
        return memo[N]

    tong = 0
    for i in range(1, N+1):
        j = i * (i + 1) * (2 * i + 1) / 6
        tong += N / j

    memo[N] = tong

    # Trả về kết quả của F(n):
    return tong


N = int(input("N = "))
#Tạo mảng gồm N+1 phần tử 0, dùng để lưu trữ các số hạng đã tính trước đó 
memo = [0]*(N+1)
result = F(N,memo)
print("F(%d) = %.7f" %(N,result))