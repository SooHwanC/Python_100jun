N = int(input())
init = 1
i = 1
while True:
    if N <= init:
        print(i)
        break
    else:
        init += i * 6
        i += 1