n = int(input())
for i in range(1, n+1):
    d = i * i
    g = 10 ** (len(str(i)))
    if d % g == i:
        print(f"{i}*{i}={d}")

