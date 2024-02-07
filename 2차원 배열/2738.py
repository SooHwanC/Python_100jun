N, M = map(int, input().split())

arr1 = [list(map(int, input().split())) for i in range(N)]
arr2 = [list(map(int, input().split())) for i in range(N)]

result = [[arr1[i][j] + arr2[i][j] for j in range(M)] for i in range(N)]

for i in range(N):
    for j in range(M):
        print(result[i][j], end=" ")
    print()