import math


def is_prime_number(n:int) -> bool:

    if n<2:
        return False

    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False

    return True

t = int(input())

for _ in range(t):
    s = input()
    if len(s)<4:
        print("NO")
        continue
    cnt = 0
    l = len(s)
    cnt += int(s[l - 4])
    cnt = cnt*10 + int(s[l - 3])
    cnt = cnt*10 + int(s[l - 2])
    cnt = cnt*10 + int(s[l - 1])

    print("YES" if is_prime_number(cnt) else "NO")