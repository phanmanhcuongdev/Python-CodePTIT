def USCLN(a,b):
    while b!=0:
        t = a % b
        a=b
        b=t
    return a

def isPrimeNumber(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

t = int(input())

for _ in range(t):
    n = int(input())
    cnt = 0
    for i in range(1,n):
        if USCLN(i,n)==1:
            cnt+=1
    print("YES" if isPrimeNumber(cnt) else "NO")


