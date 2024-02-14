N, B = map(int, input().split())
result = ""
while N > 0:
    if N % B >= 10:
        result += str(chr(N % B + 55))
    else:
        result += str(N % B)
    N = int(N / B)
print(result[::-1])