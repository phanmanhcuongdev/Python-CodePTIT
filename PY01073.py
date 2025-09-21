from itertools import combinations, permutations

n = input().strip()
for p in permutations(list(n)):
    print("".join(p))