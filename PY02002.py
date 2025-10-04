def fibonacci(x:int)->list:
    res=[]
    cnt = 0
    for i in range(1,x+1):
        if i==1 or i==2:
            cnt+=1
            res.append(1)
        else:
            res.append(res[i-3]+res[i-2])
            cnt+=1
    return res

t = int(input())
for _ in range(t):
    [a, b] = list(map(int, input().split()))
    result = fibonacci(b)
    for i in range(a - 1, b):
        print(result[i], end=" ")
    print()
