def plus(n:int,i:int):
    result = float(0)
    for j in range(i,n+1,2):
        result += float(1/j)
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    if n%2==0:
        result=plus(n,2)
    else:
        result=plus(n,1)
    print(f"{result:6f}")
