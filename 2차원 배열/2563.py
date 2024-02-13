arr = [[0]*100 for i in range(100)]
for i in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            arr[i][j] = 1
count = sum(sum(i) for i in arr)
print(count)