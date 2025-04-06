n = int(input("N = "))
count = 0
end = n + 1
for i in range(1,end):
    for j in range (1,end):
        for k in range (1,end):
            for m in range(1,end):
                if i+j+k+m == n:
                    count += 1
print(count)
