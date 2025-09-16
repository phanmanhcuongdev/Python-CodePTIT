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
    if len(s)<4:
        print("NO")
        continue

    head = 0;tail =0

    head += int(s[0])
    head = head*10+int(s[1])
    head = head * 10 + int(s[2])

    l = len(s)

    tail += int(s[l-3])
    tail = tail * 10 + int(s[l-2])
    tail = tail * 10 + int(s[l-1])

    print("YES" if is_prime_number(head) and is_prime_number(tail) else "NO")


