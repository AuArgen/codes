n = int(input())
arr = list(map(int,input().split()))
m=0
ind = 0
sorted(arr)
for i in range(n):
    if arr[i] > m:
        m = arr[i]
        ind = i
arr[0], arr[ind] = arr[ind], arr[0]
print(" ".join(map(str,arr)))


