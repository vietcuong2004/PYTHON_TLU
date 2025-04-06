def count_partitions(n, depth, current_sum, memo):
    if depth == 4:
        if current_sum == n:
            return 1
        return 0
    
    if memo[depth][current_sum] != -1:
        return memo[depth][current_sum]
    
    ways = 0
    for i in range(1, n + 1):
        if current_sum + i <= n:
            ways += count_partitions(n, depth + 1, current_sum + i, memo)
    
    memo[depth][current_sum] = ways
    return ways

N = int(input("Nhập số nguyên dương N: "))
memo = [[-1] * (N + 1) for _ in range(4)]
ways = count_partitions(N, 0, 0, memo)
print("Số cách phân tích số", N, "thành tổng của đúng 4 số nguyên dương là:", ways)