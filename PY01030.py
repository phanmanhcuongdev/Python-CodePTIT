def is_prime_number_together(a:int,b:int)->bool:
    while b!=0:
        t = a%b
        a=b
        b=t
    return True if a==1 else False

n, k = map(int, input().split())
s1 = int('1'+(k-1)*'0')
s2 = int('9'*k)
cnt = 0
for i in range(s1,s2+1):
    if is_prime_number_together(i,n):
        print(i,end=' ')
        cnt+=1
        if cnt%10==0:
            print()
            cnt=0

