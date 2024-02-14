for i in range(int(input())):
    C = int(input())
    print(int(C / 25), end=" ")
    C = C % 25
    print(int(C / 10), end=" ")
    C = C % 10
    print(int(C / 5), end=" ")
    C = C % 5
    print(int(C / 1))