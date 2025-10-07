def merge_count(a:list):
    if (len(a)<=1) : return a,0
    mid = len(a)//2
    L,cL = merge_count(a[:mid])
    R,cR = merge_count(a[mid:])
    i = j = 0
    merged = []
    c = cR + cL
    while i<len(L) and j<len(R):
        if L[i]<=R[j]:
            merged.append(L[i]);i+=1
        else:
            merged.append(R[j]);j+=1
            c+=len(L)-i
    merged.extend(L[i:]);merged.extend(R[j:])
    return merged,c

n = int(input().strip())
lst = list(map(int,input().split()))
_,count = merge_count(lst)
print(count)


