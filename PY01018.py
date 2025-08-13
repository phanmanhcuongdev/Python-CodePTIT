P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    line = input().strip()
    if not line:
        continue

    k_s = line.split()
    k = int(k_s[0])
    if k == 0:
        break

    s = k_s[1]

    out = []
    for ch in s:
        i = P.index(ch)
        out.append(P[(i + k) % 28])

    print(''.join(out)[::-1])
