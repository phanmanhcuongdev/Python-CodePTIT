from collections import Counter

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = list(map(int,input().split()))
        freq = Counter(lst)

        candidates = [num for num, count in freq.items() if count>n//2]

        if not candidates:
            print("NO")
        else:
            print(min(candidates))

if __name__ == '__main__':
    main()

