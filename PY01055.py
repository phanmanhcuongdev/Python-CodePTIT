t = int(input())

for _ in range(t):
    n = input()

    if len(n)<3 or len(n)%2==0:
        print("NO")
        continue

    a = n[0]
    b = n[1]

    if a==b:
        print("NO")
        continue

    check = True

    for i in range(0,len(n),2):
        if n[i]!=a:
            check = False
            break

    print("YES" if check else "NO")
