def count_partitions(n, count, depth, current_sum):
    if depth == 4:  # Đã tìm được 4 số nguyên dương
        if current_sum == n:
            count[0] += 1
        return
    
    for i in range(1, n + 1):
        if current_sum + i <= n:  # Đảm bảo không vượt quá n
            count_partitions(n, count, depth + 1, current_sum + i)

def main():
    N = int(input("Nhập số nguyên dương N: "))
    count = [0]  # Sử dụng danh sách để truyền tham chiếu
    count_partitions(N, count, 0, 0)
    print("Số cách phân tích số", N, "thành tổng của đúng 4 số nguyên dương là:", count[0])

if __name__ == "__main__":
    main()
