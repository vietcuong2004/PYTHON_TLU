def sang_snt(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    primes = [x for x in range(n + 1) if is_prime[x]]
    return primes

# Tìm tất cả các số nguyên tố nhỏ hơn 1 triệu và tạo thành tuple P
n = 1000000
primes_tuple = tuple(sang_snt(n))

# In ra số lượng các số nguyên tố và một số ví dụ để kiểm tra kết quả
print("Tổng số lượng số nguyên tố nhỏ hơn 1 triệu:", len(primes_tuple))
print(primes_tuple)  # In ra 1tr số nguyên tố 
