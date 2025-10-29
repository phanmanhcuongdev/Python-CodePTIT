import cmath
def main():
    while True:
        lst = list(map(int, input().split()))
        if lst[0] == 0 and lst[1] == 0 and lst[2] == 0 and lst[3] == 0:
            break
        cnt = 0
        while lst[0] != lst[1] or lst[1]!= lst[2] or lst[2]!= lst[3]:
            x1 = abs(lst[0] - lst[1])
            x2 = abs(lst[1] - lst[2])
            x3 = abs(lst[2] - lst[3])
            x4 = abs(lst[3] - lst[0])
            lst = [x1,x2,x3,x4]
            cnt+=1
        print(cnt)


if __name__ == "__main__":
    main()