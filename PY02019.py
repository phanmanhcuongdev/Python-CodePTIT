
def soNguyenToCungNhau(a:int,b:int):
    while b!=0:
        t = a%b
        a = b
        b = t
    return True if a==1 else False

def main():
    n = int(input())
    lst = list(map(int,input().split()))
    lst = sorted(lst)
    for i in range(n):
        for j in range(i+1,n):
            if soNguyenToCungNhau(lst[i],lst[j]):
                print(f"{lst[i]} {lst[j]}")

if __name__ == '__main__':
    main()