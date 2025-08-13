import math
from sys import is_finalizing

t = int(input())

for _ in range(t):
    s1 = input().strip()
    s2 = s1[::-1]
    check = True
    for i in range(1,len(s1)):
        if abs(ord(s1[i])-ord(s1[i-1])) != abs(ord(s2[i])-ord(s2[i-1])):
            check = False
            break
    print("YES" if check else "NO")