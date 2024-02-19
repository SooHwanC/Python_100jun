# num = 1
# cycle = -1
# X = int(input())
# count = 0

# while True:
#     j = num
#     if cycle == 1:
#         for i in range(0, j, +1):
#             count += 1
#             if count == X:
#                 print(f"{i + 1}/{j}")
#                 break
#             j -= 1
#         if count == X:
#             break
#     else:
#         for i in range(0, j, +1):
#             count += 1
#             if count == X:
#                 print(f"{j}/{i + 1}")
#                 break
#             j -= 1
#         if count == X:
#             break
#     num += 1
#     cycle *= -1

######################################


X = int(input())
count = 0

for j in range(1, X + 1):
    count += j
    if count >= X:
        if (j % 2) == 0:
            print(f"{j - (count - X)}/{count - X + 1}")
        else:
            print(f"{count - X + 1}/{j - (count - X)}")
        break