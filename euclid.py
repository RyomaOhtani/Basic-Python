import numpy as np
# a = int(input("a の値を入力: "))
# b = int(input("b の値を入力: "))

# # TODO

# # ユーグリッドの互除法
# def gcd(x, y):
#     while y != 0:
#         x, y = y, x % y
#     return x

# gcd_value = gcd(a, b)

# if gcd_value == 1:
#     print(f"{a}と{b}は互いに素です")
# else:
#     print(f"{a}と{b}の最大公約数は{gcd_value}であるため,互いに素ではありません")

# def greet(name):
#     print(f"Hello, {name}") # f-string  f"文字列{変数名}" 
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 100)  # Generate x values from -2π to 2π
y = np.sin(x)  # Calculate sin(x) values

plt.plot(x, y)  # Plot the graph
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Graph of sin(x)')
plt.grid(True)
plt.show()