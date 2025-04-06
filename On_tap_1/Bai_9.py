def print_substrings(S):
    substrings = set()  # Sử dụng set để lưu trữ các chuỗi con khác nhau
    n = len(S)
    end = n+1

    # Duyệt qua từng vị trí bắt đầu của chuỗi con
    for i in range(n):
        # Duyệt qua từng vị trí kết thúc của chuỗi con
        for j in range(i + 1, end):
            substring = S[i:j]  # Lấy chuỗi con từ vị trí i đến j
            substrings.add(substring)  # Thêm chuỗi con vào set

    # In ra màn hình các chuỗi con khác nhau
    for substring in substrings:
        print(substring)

S = input("Nhập chuỗi S: ")
print_substrings(S)
