def check(n):
    for i in range(len(n)-1):
        if n[i]>n[i+1]:
            return False
    return True


t = int(input())
for _ in range(t):
    n = input().strip()
    print("YES" if check(n) else "NO")