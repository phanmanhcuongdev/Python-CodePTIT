def Sum(n):
    a = 0
    for i in n:
        a+=int(i)
        a%=10
    return True if a==0 else False

def Dis(n):
    for i in range(len(n)-1):
        if int(n[i])-int(n[i+1])!=2 and int(n[i])-int(n[i+1])!=-2:
            return False
    return True

t = int(input())
for _ in range(t):
    n = input().strip()
    print("YES" if Dis(n) and Sum(n) else "NO")
