import sys

lst = sys.stdin.read().split()
result = set()
for i in range(len(lst)):
    result.add(int(lst[i])%42)
print(len(result))
