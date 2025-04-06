f = open("Test.txt",encoding = "utf-8")
s = f.read()
words = s.split()

# In ra 1 từ dài nhất:
# longest_word = max(words,key = len)
# print(longest_word)

#In ra các từ có cùng độ dài max:
max_len = max(len(x) for x in words)
for w in words:
	if len(w) == max_len:
		print(w)