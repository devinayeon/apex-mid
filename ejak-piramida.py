from typing import Any

n: int = int(input())
a = lambda x: ''.join(chr(97 + i) for i in range(x))
b = lambda x: ''.join(str(i) for i in range(1, x + 1))
c = lambda x: a(x) + 'x' + b(x)

u = 'x' + a(n - 1) + 'x' + b(n - 1) + 'x'

print(*(
    ' ' * ((len(u) - len(s)) // 2) + s
    for s in ['x'] + [c(i) for i in range(1, n - 1)] + [u]
), sep='\n')
