arr = [list(map(int, input().split())) for i in range(9)]
max_val = -1
row_index = 0
col_index = 0
for i in range(9):
    for j in range(9):
        if max_val < arr[i][j]:
            max_val = arr[i][j]
            row_index = i+1
            col_index = j+1
print(max_val)
print(row_index, col_index)