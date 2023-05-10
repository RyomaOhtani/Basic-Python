text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

# 句読点を除去し、単語リストを得る
words = [word.strip(',.') for word in text.split()]

# 各単語の文字数を得る
char_counts = list(map(len, words))

# くっつけて整数値に変換する
num = int(''.join(map(str, char_counts)))

print(num)
