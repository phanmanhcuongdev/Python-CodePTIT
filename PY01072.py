from itertools import combinations

[n,k] = list(map(int,input().split()))
inp = list(map(int,input().split()))
my_set = set(inp)
lst = sorted(my_set)
for combo in combinations(lst, k):
    print(*combo)
