def calculate_bacteria_growth(N, H):
    for i in range(1,H+1):
        if i % 2 == 0:  # Thời điểm giờ chẵn
            N *= 2
        else:  # Thời điểm giờ lẻ
            N += min(int(N * 0.3), 30)  # Tăng tối đa 30% hoặc 30 vi khuẩn

    return int(N)  # Chuyển sang kiểu số nguyên

# Nhập số lượng vi khuẩn ban đầu (N) và thời gian (H)
N = int(input("Nhập số lượng vi khuẩn ban đầu: "))
H = int(input("Nhập thời gian (số giờ): "))

result = calculate_bacteria_growth(N, H)
print(f"Số lượng vi khuẩn sau {H} giờ: {result}")
