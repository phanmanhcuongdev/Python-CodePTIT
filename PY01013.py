import math

def USCLN(a,b):
    while(b!=0):
        t = a%b
        a=b
        b=t
    return a

def isPrimeNumber(a):
    if a<=1:
        return False
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            return False
    return True

def Sum(a):
    result = 0
    while a>0:
        result+=a%10
        a//=10
    return result

t =  int(input())

for _ in range(t):
    lst = list(map(int,input().split()))
    print("YES" if isPrimeNumber(Sum(USCLN(lst[0],lst[1]))) else "NO")


