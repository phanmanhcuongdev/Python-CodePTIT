import math


def is_prime_number(n:int)->bool:
    if n<2:
        return False

    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False

    return True

t = int(input())

for _ in range(t):
    s = input()
    cnt = 0
    for c in s:
        if c in {'2','3','5','7'}:
            cnt+=1
    print("YES" if is_prime_number(len(s)) and len(s)-cnt<cnt else "NO")