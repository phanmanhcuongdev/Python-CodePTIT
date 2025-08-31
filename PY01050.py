def dfs_len(L):
    def dfs(pos,a,b,c,buf):
        if pos == L:
            if a>=1 and b>=1 and c>=1 and a<=b<=c:
                print("".join(buf))
            return
        buf.append('A');dfs(pos+1,a+1,b,c,buf);buf.pop()
        buf.append('B');dfs(pos+1,a,b+1,c,buf);buf.pop()
        buf.append('C');dfs(pos+1,a,b,c+1,buf);buf.pop()

    dfs(0,0,0,0,[])

n = int(input())
for i in range(3,n+1):
    dfs_len(i)