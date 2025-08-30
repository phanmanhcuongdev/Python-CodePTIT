import sys

def prepare()->list:
    first = ['2','4','6','8']
    even =  ['0','2','4','6','8']

    result = []

    for i in first:
        result.append(int(i+i))

    for i in first:
        for j in even:
            result.append(int(i+j+j+i))

    for i in first:
        for j in even:
            for k in even:
                result.append(int(i+j+k+k+j+i))

    return result

PAL = prepare()
data  = list(map(int,sys.stdin.read().split()))

t = data[0]

idx = 1
out_lines = []

for _ in range(t):
    n = data[idx];idx+=1
    ans = [str(x) for x in PAL if n>x]
    out_lines.append(" ".join(ans))

print("\n".join(out_lines),end = '')
