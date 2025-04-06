# Tạo list để lưu các họ và các tên
first_names = []
last_names = []

# Nhập và xử lý chuỗi
while True:
	student = input(">> Nhập tên sinh viên: ")
	if (student == ""): break 
	else:
		name = student.split()
		first_names.append(name[0])
		last_names.append(" ".join(name[1:]))

# Dùng zip() để ghép 1 phần tử của first_names và 
# 1 phần tử của last_names thành 1 căp giá trị tuple
# VD: first_names[0] = 'Vương' 
#	  last_names[0] = 'Việt Cường'
#   => zip(first_names[0],last_names[0]) = ('Vương','Việt Cường')

# In ra danh sách họ và tên
print("\n>> Danh sách họ và tên của các sinh viên trong lớp:")
print('{:_^10}'.format('Họ') ,"|",'{:_^11}'.format('Tên'), sep = "")
for first_names, last_names in zip(first_names, last_names):
    print("%s\t\t%s" %(first_names,last_names))