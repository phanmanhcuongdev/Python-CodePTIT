t = int(input().strip())
for _ in range(t):
    n = input().strip()
    cnt = 0
    for i in n:
        cnt+=(ord(i)-48)
    print("YES" if str(cnt)==str(cnt)[::-1] and cnt>10 else "NO")