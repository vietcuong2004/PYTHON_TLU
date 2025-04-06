def find_last_person(n):
    # Tìm số cuối cùng được loại khỏi bàn
    last_person = 0

    for i in range(1, n):
        last_person = (last_person + 3) % (i + 1)

    # Trả về người cuối cùng còn lại
    return last_person + 1

n = int(input("So nguoi ngoi quanh ban: "))

# Gọi hàm và in kết quả
last_person = find_last_person(n)
print("Nguoi o lai cuoi cung la nguoi thu", last_person)
 