t = int(input())
for _ in range(t):
    s = input().strip()
    print("YES" if set(s) <= {'0','1','2'} else "NO")
