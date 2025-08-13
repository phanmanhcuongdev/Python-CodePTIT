import math

def solve(n : int):
    if n==1:
        return [1]
    lst = []
    lst.append("1")
    for i in range(2,int(math.sqrt(n))):
        cnt = 0
        while n%i==0:
            cnt+=1
            n//=i
        if cnt!=0:
            lst.append(f"{i}^{cnt}")
    if n!=1:
        lst.append(f"{n}^{1}")
    return lst


t = int(input())
for _ in range(t):
    n = int(input())
    print(" * ".join(solve(n)))
