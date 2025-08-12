t = int(input())

for _ in range(t):
    s = input().strip()
    result = float('inf')
    temp = ''

    for ch in s:
        if ch.isdigit():
            temp += ch
        else:
            if temp:
                result = min(result, int(temp))
                temp = ''
    if temp:
        result = min(result, int(temp))

    print(0 if result == float('inf') else result)
