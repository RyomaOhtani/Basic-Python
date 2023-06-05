a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO

# ユーグリッドの互除法
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

gcd_value = gcd(a, b)

if gcd_value == 1:
    print(f"{a}と{b}は互いに素です")
else:
    print(f"{a}と{b}の最大公約数は{gcd_value}であるため,互いに素ではありません")