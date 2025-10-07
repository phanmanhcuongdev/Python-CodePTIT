n = int(input().strip())
lst = list(map(int,input().split()))
result = 0
for i in range(n-1):
    if lst[i]!=lst[i+1]:
        result+=1
    else:
        continue
print(result)