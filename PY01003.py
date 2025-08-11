t = int(input())
for i in range(t):
    n = int(input())
    m = 10
    while n > m:
        n = ((n+m//2)//m)*m
        m *= 10
    print(n)