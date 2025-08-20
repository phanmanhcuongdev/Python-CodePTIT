t = int(input())
for _ in range(t):
    n = input()
    check = True
    if len(n)==1:
        print("NO")
        continue
    a = n[0]
    b = n[1]
    for i in range(2,len(n)):
        if i%2==0:
            if n[i]!=a:
                check = False
                break
        else:
            if n[i]!=b:
                check = False
                break
    print("YES" if check else "NO")

