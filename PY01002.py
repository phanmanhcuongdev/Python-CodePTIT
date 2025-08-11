sen = input().replace(" ", "")

x = int(sen[0])
y = int(sen[2])
z = int(sen[4])
ops = sen[1]

if ops == "+":
    print("YES" if x + y == z else "NO")
elif ops == "-":
    print("YES" if x - y == z else "NO")
elif ops == "*":
    print("YES" if x * y == z else "NO")
else:
    print("YES" if x / y == z else "NO")
