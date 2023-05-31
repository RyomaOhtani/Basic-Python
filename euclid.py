a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO

# ユーグリッドの互除法
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# a > b になるように入れ替え
if a < b:
    a, b = b, a

GCD = gcd(a, b)
print(GCD)
