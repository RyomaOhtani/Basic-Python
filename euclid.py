a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO

# ユーグリッドの互除法
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# 値の維持
aa = a
bb = b

# a > b になるように入れ替え
if a < b:
    a, b = b, a

GCD = gcd(a, b)

# 元の値に戻す
a=aa
b=bb

if GCD == 1:
    print(a, "と", b, "は互いに素です")
else:
    print(a, "と", b, "の最大公約数は",GCD, "であるため,互いに素ではありません")