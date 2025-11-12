def main():
    n = int(input())
    lst = list(map(int,input().split()))
    s = set(lst)
    for i in range(1,n+2):
        if i not in s:
            print(i)
            break

if __name__ == '__main__':
    main()