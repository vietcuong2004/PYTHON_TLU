from math import sqrt
def prime_factors(N):
    factors = []
    divisor = 2 #Thừa số nguyên tố
    end = sqrt(N)
    while divisor <= end:
        if N % divisor == 0:
            factors.append(divisor)
            N //= divisor
        else:
            divisor += 1

    if N > 1:
        factors.append(N)

    return factors

N = int(input("N = "))
result = prime_factors(N)
if len(result) > 1:
    print(f"Phân tích {N} thành các thừa số nguyên tố là:", " x ".join(map(str, result)))
else:
    print(f"{N} là số nguyên tố.")
