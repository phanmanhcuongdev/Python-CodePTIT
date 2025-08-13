t = int(input())
for _ in range(t):
    n = input().strip()
    chars = list(n)
    result = ""
    for x in range(len(n)):
        if not chars[x].isdigit():
            temp = chars[x]
        else:
            dup = int(chars[x])
            result+=(temp*dup)
    print(result)
