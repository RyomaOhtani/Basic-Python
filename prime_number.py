# TODO

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

def check_prime():
    a = input("nの値を入力")
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

check_prime()