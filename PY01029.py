def PrimeTogether(a,b):
    while b!=0:
        t = a%b
        a=b
        b=t
    return "YES" if a==1 else "NO"

t = int(input())
for _ in range(t):
    n = input()
    print(PrimeTogether(int(n),int(n[::-1])))