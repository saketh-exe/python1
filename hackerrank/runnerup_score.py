n = int(input())
arr = set(map(int, input().split()))
s = max(arr)
arr.remove(s)
print(max(arr))