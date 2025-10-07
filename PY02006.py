t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    a.sort();b.sort()
    result = True
    for i in range(n):
        if a[i]>b[i]:
            result = False
            break
    print("YES" if result else "NO")