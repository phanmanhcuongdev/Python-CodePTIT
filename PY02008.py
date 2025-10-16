import math

def first_n_primes(n: int):
    if n == 0: return []
    if n < 6:
        small = [2,3,5,7,11]
        return small[:n]
    N = int(n*(math.log(n) + math.log(math.log(n)))) + 10  # cận trên + đệm
    sieve = bytearray(b"\x01")*(N+1)
    sieve[0:2] = b"\x00\x00"
    p = 2
    while p*p <= N:
        if sieve[p]:
            step = p
            start = p*p
            sieve[start:N+1:step] = b"\x00"*(((N - start)//step)+1)
        p += 1
    primes = [i for i, is_p in enumerate(sieve) if is_p]
    return primes[:n]

[a,b] = list(map(int,input().split()))
print(b,end = " ")
for c in first_n_primes(a):
    b = b+c
    print(b,end = ' ' )
print()