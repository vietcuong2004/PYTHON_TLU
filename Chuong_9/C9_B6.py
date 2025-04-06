f = open("Test.txt",encoding = "utf-8")
s = f.read()
# Các từ có trong file:
words = s.split()

# Đếm số lần xuất hiện của các từ:
a = set(words)
count_words = {}
for x in a:
	count = words.count(x)
	count_words[x] = count

# Sắp xếp giảm dần theo số lần xuất hiện:
sorted_words = sorted(count_words.keys(),key = lambda x:count_words[x], reverse = True)

# In ra kết quả:
for x in sorted_words:
	print(x,":",count_words[x])