T = int(input())
for i in range(T):
    RS = input()
    R = int(RS.split()[0])
    S = RS.split()[1]
    for j in range(len(S)):
        print(S[j]*R, end="")
    print()