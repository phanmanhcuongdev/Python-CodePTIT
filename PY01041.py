import sys

def isIncreOrDecre(m:str)->bool:
    if len(m)<3:
        return False

    cnt = 0

    if m[0]>m[1]:
        cnt =1
    elif m[0]==m[1]:
        return False

    for i in range(1,len(m)-1):
        if cnt>=2:
            return False
        if m[i]>m[i+1] and cnt==1:
            continue
        elif m[i]<m[i+1] and cnt == 0:
            continue
        else:
            cnt+=1
    return True


tokens = sys.stdin.read().split()
it = iter(tokens)

t = int(next(it))

for _ in range(t):
    n = next(it)
    print("YES" if isIncreOrDecre(n) else "NO")
