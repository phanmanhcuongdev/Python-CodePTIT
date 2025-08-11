t = int(input())
for _ in range(t):
    n = input()
    a = int(n[0]+n[1])
    b = int(n[len(n)-2]+n[len(n)-1])
    print("YES" if a==b else "NO")