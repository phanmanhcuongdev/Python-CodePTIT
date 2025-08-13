def convert_bin_to_base(x:str,b:int)-> str:
    if b==2:
        return x.lstrip('0') or '0'
    kmap = {4:2,8:3,16:4}
    k = kmap[b]
    pad = (-len(x))%k
    x = '0'*pad + x
    parts = [x[i:i+k] for i in range(0,len(x),k)]
    digits = []
    for p in parts:
        v = int(p,2)
        if v<10:
            digits.append(str(v))
        else:
            digits.append(chr(ord('A')+v-10))
    out = ''.join(digits).lstrip('0') or '0'
    return out



t = int(input())

for _ in range(t):
    base = int(input())
    n = input()
    print(convert_bin_to_base(n,base))
