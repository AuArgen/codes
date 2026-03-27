
n = int(input())
f = True
a = 0
q = n
while f:
    q += q % 2
    q = q // 2
    if q % 2: break
    q += 1
    a+=1
print(a)
for i in range(1, n+1, 2):
    g = []
    for j in range(i, n+1, 2):
        g.append(j)
        if sum(g) == n:
            print(g)
            break
