def money(n,m):
    if n % 100 != 0:
        return 0
    d = 0
    for a1 in range (n//5000,-1,-1): #Giảm dần
        n1 = n - a1 * 5000 # n1: số tiền còn lại sau khi lấy a1 tờ 5k
        if a1 > m: break # Số tờ 5k vượt quá m thì dừng lại
        for a2 in range (n1//2000,-1,-1):
            n2 = n1 - a2 * 2000
            if a1 + a2 > m: break
            for a3 in range (n2//1000,-1,-1):
                n3 = n2 - 1000 * a3
                if a1 + a2 + a3 > m:break
                for a4 in range (0 if n3 % 200 == 0 else 1,n3//500 +1,2):
                    n4 = n3 - a4 * 500
                    a5 = n4//200
                    if a1 + a2 + a3 + a4 + a5 <= m: d += 1
    return d 

n = int(input('N = '))
m = int(input('M = '))
result = money(n,m)
print("Co %d phuong an doi tien" %result)
