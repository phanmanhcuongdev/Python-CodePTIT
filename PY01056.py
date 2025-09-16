import math


def is_prime_number(n:int) -> bool:

    if n<2:
        return False

    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False

    return True

def is_even_pos_even(n:str) -> bool:

    for i in range(1,len(n),2):
        if int(n[i]) % 2 == 0:
            return False

    return True


def is_odd_pos_odd(n: str) -> bool:
    for i in range(0, len(n), 2):
        if int(n[i]) % 2 != 0:
            return False

    return True

t = int(input())

for _ in range(t):

    s = input()
    cnt = 0
    for c in s:
        cnt+=int(c)

    print("YES" if is_prime_number(cnt) and is_odd_pos_odd(s) and is_even_pos_even(s) else "NO")