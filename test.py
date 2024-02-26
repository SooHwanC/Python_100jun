while True:
    arr = []
    n = int(input())
    if n == -1:
        break
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
    total_sum = sum(arr)
    if n == total_sum:
        print(n, "=", " + ".join(map(str, arr)))
    else:
        print(f"{n} is NOT perfect.")