# def find_primes(n):
#     primes = []
#     for num in range(2, n + 1):
#         is_prime = True
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
#     return primes


def find_primes(n):
    primes = []
    sieve = [True] * (n+1) 
    for p in range(2, n+1): 
        if sieve[p]:  
            primes.append(p)
            for i in range(p*p, n+1, p): 
                sieve[i] = False
    return primes

N = int(input())
primes = find_primes(N)
index = 0
while N != 1:
    if N % primes[index] == 0:
        print(primes[index])
        N //= primes[index]
    else:
        index += 1