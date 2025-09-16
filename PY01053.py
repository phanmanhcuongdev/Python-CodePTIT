t = int(input())

for _ in range(t):
    n = input()
    sum = 0
    for c in n:
        sum+=int(c)
    if sum%3==0:
        print("YES")
    else:
        print("NO")