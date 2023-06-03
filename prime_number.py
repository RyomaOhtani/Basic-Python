a = input("nの値を入力: ")

# TODO

def is_prime(N):
    if N <= 1:
        return False

    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            return False

    return True

try:
#　入力された値がfloat型の場合int型にする
    n = int(float(a))
# 0と正の整数以外を除外する
    if n <= 0 or n != float(a):
        raise ValueError
    if is_prime(n):
        print(a, "は素数です")
    else:
        print(a, "は素数ではありません")
# 正の整数以外が入力された時のエラーメッセージ
except ValueError:
    print("nの値は正の整数を入力してください")

