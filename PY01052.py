import math

def is_prime_number(n:int)->bool:
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return  False
    return True

t = int(input())
for _ in range(t):
    n = input().strip()
    cnt = 0
    for i in n:
        cnt+=(ord(i)-48)
    print("YES" if is_prime_number(cnt) else "NO")