n: int
k: int
l: int
r: int

n, k, l, r = map(int, input().split())
a: list[int] = [*map(int, input().split())]

print(sum(i + j <= n and sum(a[i:i + j]) == k and any(x < 0 for x in a[i:i + j]) for i in range(n) for j in range(l, r + 1)))
