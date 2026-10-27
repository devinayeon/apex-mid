n: int = int(input())
v: list[int] = [1]

for _ in range(n):
    print(*v); v = [1, *map(sum, zip(v, v[1:])), 1]
