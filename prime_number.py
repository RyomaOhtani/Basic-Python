a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

# TODO
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

if is_prime(a):
    print(a, "は素数です")
else:
    print(a, "は素数ではありません")

if is_prime(b):
    print(b, "は素数です")
else:
    print(b, "は素数ではありません")