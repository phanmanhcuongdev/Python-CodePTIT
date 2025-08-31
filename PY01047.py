import math

def isPrimeNumber(n:int)->bool:
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return  False
    return True

t = int(input())
for _ in range(t):
    n = input().strip()
    check = True
    if len(n)<4:
        check = isPrimeNumber(int(n))
    else:
        check = isPrimeNumber(int(n[len(n)-4::]))

    print("YES" if check else "NO")