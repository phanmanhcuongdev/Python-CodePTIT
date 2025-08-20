def reverse_and_sum(n:int):
    for i in range(1000):
        if n%7==0:
            return n
        else:
            n= int(str(n)[::-1])+n
    return -1

t = int(input())
for _ in range(t):
    n = int(input())
    print(reverse_and_sum(n))