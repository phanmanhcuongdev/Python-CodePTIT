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
    n = input()
    result = True
    for i in range(0,len(n)):
        if not (((n[i] in {'2','3','5','7'}) and is_prime_number(i)) or ((n[i] not in {'2','3','5','7'}) and not is_prime_number(i))):
            result = False
            break
    print("YES" if result else "NO")