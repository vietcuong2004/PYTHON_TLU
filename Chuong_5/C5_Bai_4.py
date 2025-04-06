def Valid_Email (email):
	# Kiểm tra email phải chứa ký tự @ và không nằm ở vị trí đầu hoặc cuối
    if "@" not in email or email.startswith("@") or email.endswith("@"):
        return False

    # Tách email thành hai phần, tên người dùng và tên miền
    username, domain = email.split("@", 1)

    # Kiểm tra xem tên người dùng và tên miền không trống
    if not username or not domain:
        return False

    # Kiểm tra xem tên miền phải chứa ít nhất một dấu chấm (.)
    if "." not in domain:
        return False

    return True

email = input("Nhập Email: ")
if (Valid_Email(email) == True):
	print ("Email hợp lệ")
else:
	print ("Email không hợp lệ")