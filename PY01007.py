t = int(input())

for _ in range(t):
    cnt = 0
    ipt = input().split()
    n = float(ipt[0])
    x = float(ipt[1])/100.0
    m = float(ipt[2])
    while n<m:
        cnt+=1
        n=n+n*x
    print(cnt)