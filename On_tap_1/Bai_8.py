def timkiem(S):
  a = []
  for i in range(len(S)):
    for j in range(i, len(S)):
      a.append(S[i:j+1])

  return a
S = input("Nhập chuỗi S: ")

a = timkiem(S)
p = set(a)
print("Các chuỗi con khác nhau của S là:", p)
