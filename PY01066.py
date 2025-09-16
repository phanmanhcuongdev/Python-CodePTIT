t = int(input())

for _ in range(t):
    s = input()
    sa = s[::-1]
    result = True
    for i in range(0,len(s)-1):
        if abs(ord(s[i])-ord(s[i+1]))!=abs(ord(sa[i])-ord(sa[i+1])):
            result = False
            break

    print("YES" if result else "NO")