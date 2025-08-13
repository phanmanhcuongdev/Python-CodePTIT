import math

def isPrimenumber(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def Sum(n):
    result = 0
    while n>0:
        result+=n%10
        n//=10
    return result

def isAllPrimeNumber(n):
    while n>0:
        if isPrimenumber(n%10)==False:
            return False
        n//=10
    return True

t = int(input())
for _ in range(t):
    n = input()
    s1=int(n)
    s2=int(n[::-1])
    print("Yes" if isPrimenumber(s1) and isPrimenumber(s2) and isPrimenumber(Sum(s1)) and isAllPrimeNumber(s1) else "No")