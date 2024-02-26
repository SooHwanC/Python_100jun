def find(num):
    for i in range(2, num):
        if num % i == 0:
            return 0
    if num == 1:
        return 0


N = int(input())
M = list(map(int, input().split()))
count = 0
for i in range(N):
    if find(M[i]) != 0:
        count += 1
print(count)