import bisect

def generate_hamming(limit=10**18):
    res=[1]
    i2 = i3 = i5 = 0
    while True:
        next_val = min(res[i2]*2, res[i3]*3, res[i5]*5)
        if next_val > limit:
            break
        res.append(next_val)
        if next_val == res[i2] * 2:
            i2 += 1
        if next_val == res[i3] * 3:
            i3 += 1
        if next_val == res[i5] * 5:
            i5 += 1
    return res

def is_hamming(n:int)->bool:
    for p in [2,3,5]:
        while n%p==0:
            n//=p
    return n==1

hamming = generate_hamming()

t = int(input())

for _ in range(t):
    n = int(input())

    if not is_hamming(n):
        print("Not in sequence")
    else:
        idx = bisect.bisect_left(hamming,n)
        if idx < len(hamming) and hamming[idx]==n:
            print(idx+1)
        else:
            print("Not in sequence")
