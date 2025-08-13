t = int(input())
for _ in range(t):
    n = input().strip()
    temp = n[0]
    cnt = 1
    result = ""
    for i in range(1, len(n)):
        if n[i] == temp:
            cnt += 1
        else:
            result +=str(cnt) + temp
            temp = n[i]
            cnt = 1

    result += str(cnt) + temp
    print(result)
