t = int(input())

for _ in range(t):
    s = input().strip()
    result = -999
    temp = ''

    for ch in s:
        if ch.isdigit():
            temp += ch
        else:
            if temp:
                result = max(result, int(temp))
                temp = ''
    if temp:
        result = max(result, int(temp))

    print(0 if result == -999 else result)
