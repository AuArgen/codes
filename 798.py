n = int(input())
m = []
for i in range(1, n+1):
    d = i
    flag = True
    while d > 0:
        digit = d % 10
        d //= 10
        if digit == 0 or  i % digit != 0:
            flag = False
            break
    if flag:
        m.append(str(i))

print(" ".join(m))


