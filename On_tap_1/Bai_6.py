def find_min_difference_subsequence(C, N):
    min_difference = float('inf')
    result_subsequence = ""

    for i in range(len(C) - N + 1):
        subsequence = C[i:i+N]
        max_digit = max(subsequence)
        min_digit = min(subsequence)
        difference = int(max_digit) - int(min_digit)

        if difference < min_difference:
            min_difference = difference
            result_subsequence = subsequence

    return result_subsequence

C = input("Nhập dãy chữ số C: ")
N = int(input("Nhập số nguyên N: "))

result = find_min_difference_subsequence(C, N)
print("Dãy con có chênh lệch bé nhất:", result)
