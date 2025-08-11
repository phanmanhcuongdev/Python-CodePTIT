t = int(input())

for _ in range(t):
    check = True
    n = input()
    for i in range(len(n)):
        if(n[i]!="4" and n[i]!="7"):
            print("NO")
            check = False
            break
    if check : print("YES")