s = input()
cnt = 0
for i in range(len(s)):
    if 'a'<=s[i]<='z':
       cnt+=1
if cnt>=(len(s)-cnt):
    print(s.lower())
else:
    print(s.upper())