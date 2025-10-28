t = int(input())
for _ in range(t):
    n = int(input())
    lst = []
    for __ in range(n):
        x = int(input())
        lst.append(x)

    freq = [0] * 1001
    for x in lst:
        if 1 <= x <= 1000:
            freq[x] += 1

    max_freq = max(freq)
    for v in range(1, 1001):
        if freq[v] == max_freq:
            print(v)
            break
