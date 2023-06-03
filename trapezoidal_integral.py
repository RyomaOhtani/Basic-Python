from sympy import symbols, sympify
# --example--
# print(sin(0))
# >>> 0
# -----------

N = int(input("分割数を入力してください: ") or 100)

# 実数以外（pi等）に対応するためsympifyを使いました
a = sympify(input("積分区間の下限値を入力してください: ") or "0")
b = sympify(input("積分区間の上限値を入力してください: ") or "1")

# 変数xを定義
x = symbols("x")

expression = input("関数f(x)の式を入力してください: ")

# 関数f(x)を定義
f = sympify(expression)

# 台形積分　sympyを用いたため、f.subsで変数置換を行った
h = (b - a) / N
S = (h / 2) * (f.subs(x, a) + 2 * sum(f.subs(x, a + h * i) for i in range(1, N)) + f.subs(x, b)) 
    
print(float(S))