N = int(input())
clc = 3
for i in range(N - 1):
    clc += clc - 1
print(clc * clc)