import math

def isPrimeNumber(n:int)->bool:
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return  False
    return True

PrimeNumber = ['2','3','5','7']

t = int(input())

for _ in range(t):
    n = input()
    cnt = 0
    for i in n:
        if i in PrimeNumber:
            cnt+=1

    print("YES" if len(n)-cnt<cnt and isPrimeNumber(len(n)) else "NO")
