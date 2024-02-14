count = int(input())
num1 = count - 1
for i in range(1, count * 2, +2):
    print(" " * num1, "*" * i)
    num1 -= 1
num1 += 2
for i in range((count * 2) - 3, 0, -2):
    print(" " * num1, "*" * i)
    num1 += 1