n = input()
cnt=0
for i in range(len(n)):
    if n[i]=="4" or n[i]=="7":
        cnt+=1
print("YES" if cnt==4 or cnt==7 else "NO")