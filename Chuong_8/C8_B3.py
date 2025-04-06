prev_num = None
prev_count = 0
even_count = 0

while True:
    try:
        num_str = input("Nhập một số nguyên dương (0 để kết thúc): ")

        if num_str == '0':
            break

        if not num_str.isdigit():
            raise ValueError("Lỗi nhập số")

        num = int(num_str)
            
        if num < 0:
            raise ValueError("Lỗi số âm!!")
            
        if num == prev_num:
            prev_count += 1
            if prev_count >= 4:
                raise ValueError("Lỗi nhập lặp")
        else:
            prev_num = num
            prev_count = 1
            
        if num % 2 == 0:
            even_count += 1
            if even_count >= 5:
                raise ValueError("Lỗi nhập chẵn")
        else:
            even_count = 0
            
    except ValueError as ve:
        print(f"Phát sinh exception: {ve}")
        continue
    '''except Exception as e:
        print(f"Phát sinh exception: {e}")
        break'''
