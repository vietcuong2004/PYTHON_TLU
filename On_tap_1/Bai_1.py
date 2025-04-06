n = int(input("N = "))
end1 = n//3+1
end2 = n//5+1
A = [3*i for i in range(1,end1) if 3*i < n]
B = [5*i for i in range(1,end2) if 5*i < n]
print("tong cac so:",sum(A) + sum (B))
