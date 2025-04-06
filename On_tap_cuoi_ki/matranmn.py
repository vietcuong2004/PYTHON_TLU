def count_paths(M, N):
    # Khởi tạo ma trận DP có kích thước M+1 x N+1 với tất cả giá trị ban đầu là 0.
    dp = [[0] * (N + 1) for _ in range(M + 1)]
    
    # Khởi tạo điểm xuất phát là 1.
    dp[0][0] = 1
    
    # Tính toán số cách di chuyển cho từng ô trong lưới.
    for i in range(M + 1):
        for j in range(N + 1):
            if i > 0:
                dp[i][j] += dp[i - 1][j]  # Di chuyển từ ô phía trên
            if j > 0:
                dp[i][j] += dp[i][j - 1]  # Di chuyển từ ô bên trái
    
    # Trả về số cách di chuyển tới ô cuối cùng (M, N).
    return dp[M][N]

# Nhập giá trị M và N
M = int(input("Nhập giá trị M: "))
N = int(input("Nhập giá trị N: "))

# Tính và in số cách di chuyển
print("Số cách di chuyển:", count_paths(M, N))
