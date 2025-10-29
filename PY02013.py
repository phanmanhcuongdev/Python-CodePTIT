def change(n:int)->list:
    lst = [n]
    while n!=1:
        if n % 2 == 0:
            n //= 2
            lst.append(n)
        else:
            n = n * 3 + 1
            lst.append(n)
    return lst

def main():
    while True:
        n = int(input())
        if n==0:
            break
        print(len(change(n)))
    return 0

if __name__ == "__main__":
    main()