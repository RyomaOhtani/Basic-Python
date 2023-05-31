from math import sin, pi
# --example--
# print(sin(0))
# >>> 0
# -----------

def f(x):
    return sin(x)

N = 100

a = 0
b = 1 / 2 * pi
h = (b - a) / N

S = (h / 2) * (f(a) + 2 * sum(f(a + h * i) for i in range(1, N)) + f(b))

print(S)