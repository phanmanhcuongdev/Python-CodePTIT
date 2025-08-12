a,k,n = map(int,input().split())

r = -a%k
if r==0:
    r=k

if a+r>n:
    print(-1)
else:
    result = list(range(r,n-a+1,k))
    print(*result)