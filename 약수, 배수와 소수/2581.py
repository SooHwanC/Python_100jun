def find(num):
    for i in range(2, num):
        if num % i == 0:
            return 0
    if num == 1:
        return 0


M = int(input())
N = int(input())
arr = []
for i in range(M, N + 1):
    if find(i) != 0:
        arr.append(i)
if len(arr) == 0:
    print("-1")
else:
    print(sum(arr))
    print(min(arr))