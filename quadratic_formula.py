# (1)
a = 1
b = -6
c = 9
# 解の公式
x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
print(x1, x2)

# (2)
a = 1
b = 2
c = -8
# 解の公式
x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
print(x1, x2)

# (3)
a = 8
b = -6
c = -35
x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
#分数表示にしたいので,fractionsを使う
from fractions import Fraction
X1 = Fraction(x1)
X2 = Fraction(x2)
print(X1, X2)


# (4)
a = 1
b = 0
c = 1

# 解の公式
import cmath
x1 = (-b + cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
x2 = (-b - cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

print(x1, x2)
