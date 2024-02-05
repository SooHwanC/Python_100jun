arr = [1, 1, 2, 2, 2, 8]
A = input().split()
count = 0
for i in arr:
    print(int(i) - int(A[count]), end=" ")
    count += 1