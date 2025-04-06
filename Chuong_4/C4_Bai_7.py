def max_number(S, N):
    # Ngăn xếp rỗng để lưu trữ các chữ số của số cần tìm
    stack = []

    # Thực hiện xóa các chữ số: 
    # Nếu chữ số đang xét có giá trị lớn hơn chữ số ở đỉnh stack => Xóa đi
    # Thực hiện cho đến khi nào N=0 hoặc stack rỗng thì dừng
    for char in S:
        while N > 0 and len(stack)!=0 and (int(char) > int(stack[-1])):
            stack.pop()
            N -= 1
        #Thêm kí đã kiểm tra của S vào stack
        stack.append(char)

    # Xóa N kí tự cuối cùng nếu N vẫn còn lớn hơn 0
    while N > 0:
        stack.pop()
        N -= 1

    return "".join(stack) # Ghép các phần tử của stack lại để ra kết quả cuối cùng

# Tính toán, in kết quả
S = input("Nhập chuỗi số S: ")
N = int(input("Nhập N: "))
result = max_number(S, N)
print("Chuỗi lớn nhất sau khi xóa", N, "kí tự là:", result)
