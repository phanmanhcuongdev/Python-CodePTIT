t = int(input())

for _ in range(t):
    n = input()
    multi = 1
    for c in n:
        if c=='0':
            continue
        multi *= int(c)
    print(multi)