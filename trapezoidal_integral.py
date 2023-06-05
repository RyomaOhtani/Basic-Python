from sympy import sin, pi, exp, sqrt, symbols
# --example--
# print(sin(0))
# >>> 0
# -----------

# n:分割数, l:区間下限, u:区間上限
def d(n=100, l=0, u=1):

    def a(l):
        return l

    def b(u):
        return u

# 変数xを定義
    x = symbols("x")

# 台形積分
    h = (b(u) - a(l)) / n
    S = (h / 2) * (f.subs(x, a(l)) + 2 * sum(f.subs(x, a(l) + h * i) for i in range(1, n)) + f.subs(x, b(u))) 

    return S

x = symbols("x")

# (1)
n = 50
l = 0
u = pi / 2
f = sin(x)

result = d(n, l, u) 
print("(1)", float(result))

# (2)
n = 100
l = 0
u = 1
f = 4 / (1 + x**2)

result = d(n, l, u) 
print("(2)", float(result))

# (3)
n = 1000
l = -100
u = 100
f = sqrt(pi)*exp(-x**2)

result = d(n, l, u) 
print("(3)", float(result))