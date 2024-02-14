N, B = map(str, input().split())
listN = list(N)
result = 0
for i in range(len(listN)):
    if listN[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        result += (ord(listN[i]) - 55) * (int(B) ** (len(listN) - (i + 1)))
    else:
        result += int(listN[i]) * (int(B) ** (len(listN) - (i + 1)))
print(result)