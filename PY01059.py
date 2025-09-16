t = int(input())

for _ in range(t):
    s = input()
    sumAll = 0;mulAll=1

    isAll0 = True

    for i in range(len(s)):
        if i%2!=0:
            if s[i]!='0':
                isAll0 = False
                mulAll*= int(s[i])
        else:
            sumAll+=int(s[i])

    print(f"{sumAll} 0" if isAll0 else f"{sumAll} {mulAll}")