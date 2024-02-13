arr = [[0 for i in range(100)] for i in range(100)]

# 입력 받기
for i in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            arr[i][j] = 1
    
# 값이 1인 것의 수 세기
count = sum(sum(row) for row in arr)

# 결과 출력
print(count)
